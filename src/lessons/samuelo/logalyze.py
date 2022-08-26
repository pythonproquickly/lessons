<<<<<<< HEAD
"""
to run:
pip install -r requirements.txt
python logalyze.py

be sure to set PATH to the parent directory of all your log files

Ran 'getlogs' in 1112.1063 secs 1909 files

REQUIREMENTS:
Ok...so we're looking at files from August 1, 2021 to July 31, 2022. 
A full first month would be that it has a record for each day of August, 2021 
(i.e. 31 records/flies) and a full last month would have 31 records/files for 
July 31. My logic being that a file/record is produced for every day the 
website is onsite even if there is no traffic. This way we'd be excluding 
decommissioned websites.

"""

from genericpath import isdir
from urllib.request import DataHandler
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
STOP_YMD = '2022-07-31'
D = "\t"
N = '\n'
=======
from apachelogs import LogParser
from pathlib import Path
import os
import calendar
import datetime
from loguru import logger
PATH = '/Users/andy/ws/ctpsws-clients/lessons/src/lessons/samuelo/data/'
OUTPUT_FILE = PATH + "log_summary.csv"
START_YMD = '2021-08-01'
STOP_YMD = '2022-07-30'
>>>>>>> bdaf472116b866267ab46b36cc4e8e7cc06b930a
log_format = "%h %l %u %t \"%r\" %s %b \"%{Referer}i\" \"%{User-agent}i\" %D"
parser = LogParser(log_format)
analysis = []

<<<<<<< HEAD
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
        fo.write(f'server{D}host{D}agent{D}time{N}')
    with open(OUTPUT_FILE, 'a') as fa:
        for file in files:
            full_month_start = set()
            full_month_stop = set()
            this_file_write_cache = []
            days_in_month = 0
            with gzip.open(file,'r') as f:
                number_processed += 1
                # abandon when testing
                """if number_processed > 20:
                    exit(1)"""
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
                        # print(log.request_time)
                        continue
                    if not ("GET" in str(log_text)):
                        # print(str(log_text))
=======
def getlogs(files):

    with open(OUTPUT_FILE, 'w') as fo:
        fo.write("host,agent,time\n")
    with open(OUTPUT_FILE, 'a') as fa:
        for file in files:
            full_month_tracker = set()
            this_file_write_cache = []
            with open(file) as f:
                logger.info(file)
                for log_text in f:
                    log = parser.parse(log_text)
                    if log.status in (301, 302): # which? 304?
                        continue
                    if START_YMD >= str(log.request_time)[:10] >= STOP_YMD: # TZ?
>>>>>>> bdaf472116b866267ab46b36cc4e8e7cc06b930a
                        continue
                    yyyy = str(log.request_time.year)
                    mm = str(log.request_time.month+100)[1:]
                    dd = str(log.request_time.day+100)[1:]
<<<<<<< HEAD
                    """line = f'{file.stem}\t{log.remote_host}\t' \
                           f'{log.headers_in["User-Agent"]}\t{log.request_time}\n'"""
                    line = f"{str(file.stem).replace(D, '    ')}\t"
                    line += f"{str(log.remote_host).replace(D, '    ')}\t"
                    line += f"{str(log.headers_in['User-Agent']).replace(D, '    ')}\t"
                    line += f"{str(log.request_time).replace(D, '    ')}\n"
                    if len(line.split('\t')) != 4:
                        print("TABS != 4 !!!!!!")
                        print(line)
                    if f"{yyyy}-{mm}" == START_YMD[:7]:            
                        full_month_start.add(yyyy+mm+dd)
                        this_file_write_cache.append(line)
                    elif f"{yyyy}-{mm}" == STOP_YMD[:7]: 
                        full_month_stop.add(yyyy+mm+dd)
                        this_file_write_cache.append(line)
                    else:
                        fa.write(line)
                    if f"{yyyy}-{mm}" in (START_YMD[:7], STOP_YMD[:7]):
                        days_in_month = calendar.monthrange(log.request_time.year, \
                                                            log.request_time.month)[1]

                if f"{yyyy}-{mm}" in (START_YMD[:7], STOP_YMD[:7]):                             
                    if len(full_month_start) == days_in_month or len(full_month_stop) == days_in_month:
                        for line in this_file_write_cache:
                            fa.write(line)
                
=======
                    if f"{yyyy}-{mm}-{dd}" in (START_YMD, STOP_YMD):
                        full_month_tracker.add(yyyy+mm+dd)
                    this_file_write_cache.append(f'{log.remote_host}, \
                        {log.headers_in["User-Agent"]}, {log.request_time} \n')

            if f"{yyyy}-{mm}" in (START_YMD[:7], STOP_YMD[:7]):
                days_in_month = calendar.monthrange(log.request_time.year, \
                                                    log.request_time.month)[1]
                
                print(days_in_month,len(full_month_tracker), full_month_tracker, \
                    yyyy+"-"+mm, START_YMD[:7], STOP_YMD[:7])                
                if len(full_month_tracker) != days_in_month:
                    continue  
                  
            for line in this_file_write_cache:
                fa.write(line)
>>>>>>> bdaf472116b866267ab46b36cc4e8e7cc06b930a


def getfiles():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    paths = []
    for filepath in Path(PATH).rglob('*'):
<<<<<<< HEAD
        if filepath.is_dir():
            continue
=======
>>>>>>> bdaf472116b866267ab46b36cc4e8e7cc06b930a
        paths.append(filepath)
    return paths


def main():
    all_logs = getfiles()
    getlogs(all_logs)
    

if __name__ == "__main__":
    main()