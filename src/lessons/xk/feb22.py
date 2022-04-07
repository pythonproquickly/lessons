#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import csv
import concurrent.futures

import wrds

# In[2]:


conn = wrds.Connection(wrds_username="tianxu0709")

# In[3]:


OBS = -1
BATCH_SIZE = 500
MAX_WORKERS = 20

QUERY_FMT = """
SELECT transcriptid, componentorder, componenttext
FROM ciq_transcripts.ciqtranscriptcomponent
WHERE transcriptid in {ids}
;
"""

IR_PATTERN = re.compile("((investor|public|external)\s+relations?|\s+IR\s+)",
                        flags=re.IGNORECASE)

TRANSCRIPT_ROOT_PATH = "transcripts"
TRANSCRIPT_FILE_FMT = "{t_id}.txt"

TRANSCRIPT_META_PATH = "transcript_meta.csv"
TRANSCRIPT_META_HEADER = ["transcript_id", "has_ir"]

# In[4]:


GET_IDS_QUERY = """
SELECT DISTINCT transcriptid
FROM ciq_transcripts.ciqtranscriptcomponent
"""

if OBS > 0:
    GET_IDS_QUERY += f"""
    LIMIT {OBS}
    """

# This is not as fast as using row ranges with "LIMIT loc, offset" directly in the
# transcript processing, but it is safe from any race conditions that might occur
# due to duplicate transcripts and checking for those later on.
transcript_ids = (
    conn.raw_sql(GET_IDS_QUERY)["transcriptid"]
        .pipe(tuple)
)
tot_len = len(transcript_ids)
id_iter = [transcript_ids[i:i + BATCH_SIZE] for i in
           range(0, tot_len, BATCH_SIZE)]


# In[5]:


def get_and_write_transcripts(ids):
    clean_ids = tuple(ids) if len(ids) > 1 else f"({ids[0]})"
    transcript_text = (
        conn.raw_sql(QUERY_FMT.format(ids=clean_ids))
            .sort_values(["transcriptid", "componentorder"])
            .drop("componentorder", axis=1)
            .groupby("transcriptid")
            .sum()
    )

    info_list = []
    for t_id, text in transcript_text.iterrows():
        info_list.append((t_id, IR_PATTERN.search(text[0]) is not None))
        with open(TRANSCRIPT_ROOT_PATH + "/" + TRANSCRIPT_FILE_FMT.format(
                t_id=t_id), 'w') as f:
            f.write(text[0])

    return info_list


# In[6]:


if not os.path.exists(TRANSCRIPT_ROOT_PATH):
    os.mkdir(TRANSCRIPT_ROOT_PATH)

err_list = []
tot_written = 0

with open(TRANSCRIPT_META_PATH, "w") as f:
    writer = csv.writer(f)
    writer.writerow(TRANSCRIPT_META_HEADER)

    with concurrent.futures.ThreadPoolExecutor(
            max_workers=MAX_WORKERS) as executor:
        futures_list = [executor.submit(get_and_write_transcripts, ids) for ids
                        in id_iter]
        for i, future in enumerate(
                concurrent.futures.as_completed(futures_list)):
            try:
                info_list = future.result()
                tot_written += len(info_list)
                writer.writerows(info_list)
            except Exception as exc:
                print(f"{i}, Generated an exception: {exc}")
                err_list.append((i, exc))
            finally:
                print(f"{tot_written}/{tot_len}", end='\r')

len(err_list)
