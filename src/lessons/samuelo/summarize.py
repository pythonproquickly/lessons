"""
to run:
pip install -r requirements.txt
python logalyze.py

be sure to set PTH to the parent directory of all your log files

Ran 'getlogs' in 1112.1063 secs 1909 files

"""

from genericpath import isdir
from apachelogs import LogParser
import apachelogs
from pathlib import Path
import os
import gzip
import calendar
import functools
import time
from loguru import logger
import pandas as pd


logger.add("./apachexvt_{time}.log")
PATH = '/Users/andy/ws/ctpsws-clients/lessons/src/lessons/samuelo/data/'
OUTPUT_FILE = PATH + "log_summary.csv"
START_YMD = '2021-08-01'
STOP_YMD = '2022-07-30'
log_format = "%h %l %u %t \"%r\" %s %b \"%{Referer}i\" \"%{User-agent}i\" %D"
parser = LogParser(log_format)
analysis = []

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Ran {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer

@timer
def getlogs(files):
    number_processed = 0
    with open(OUTPUT_FILE, 'w') as fo:
        fo.write('server\thost\tagent\ttime\n')
    with open(OUTPUT_FILE, 'a') as fa:
        for file in files:
            full_month_tracker = set()
            this_file_write_cache = []
            days_in_month = 0
            with gzip.open(file,'r') as f:
                number_processed += 1
                print(f"Working on # {number_processed} {file.stem}...")
                for log_text in f:
                    try:
                        log = parser.parse(log_text.decode())
                    except Exception as e:
                        logger.info(e)
                        continue
                    if log.status not in (303, 304, 305) and \
                            not (200 <= log.status < 300): # and only GET 
                        continue
                    if (START_YMD >= str(log.request_time)[:10] >= STOP_YMD):
                        print(log.request_time)
                        continue
                    yyyy = str(log.request_time.year)
                    mm = str(log.request_time.month+100)[1:]
                    dd = str(log.request_time.day+100)[1:]
                    line = f'{file.stem}\t{log.remote_host}\t' \
                           f'{log.headers_in["User-Agent"]}\t{log.request_time}\n'
                    line = line.replace('"', '')
                    if f"{yyyy}-{mm}-{dd}" in (START_YMD, STOP_YMD): # NOT both
                        full_month_tracker.add(yyyy+mm+dd)
                        this_file_write_cache.append(line)
                    else:
                        fa.write(line)
                    if f"{yyyy}-{mm}" in (START_YMD[:7], STOP_YMD[:7]):
                        days_in_month = calendar.monthrange(log.request_time.year, \
                                                            log.request_time.month)[1]
                             
                if len(full_month_tracker) == days_in_month:            
                    for line in this_file_write_cache:
                        fa.write(line)
                


def getfiles():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    paths = []
    for filepath in Path(PATH).rglob('*'):
        if filepath.is_dir():
            continue
        paths.append(filepath)
    return paths


def main():
    all_logs = getfiles()
    getlogs(all_logs)
    

if __name__ == "__main__":
    main()