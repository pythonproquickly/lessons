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
PATH = '/Users/andy/ws/lessons/src/lessons/sam/data/'
OUTPUT_FILE = "log_summary.csv"
START_YMD = '2021-08-01'
STOP_YMD = '2022-07-31'
D = "\t"
N = '\n'
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
        fo.write(f'domain{D}client{D}user_agent{D}time{N}')
    with open(OUTPUT_FILE, 'a') as fa:
        for file in files:
            yyyy = ""
            mm = ""
            full_month_start = set()
            full_month_stop = set()
            this_file_write_cache = []
            days_in_month = 0
            domain = str(file)[len(PATH):]
            domain = domain[:domain.find('/')]
            print(f"Domain {domain}: working on # {number_processed} {file}...")
            with gzip.open(file,'r') as f:
                number_processed += 1
                # abandon when testing
                if number_processed > 1000:
                    exit(1)
                
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
                        continue
                    yyyy = str(log.request_time.year)
                    mm = str(log.request_time.month+100)[1:]
                    dd = str(log.request_time.day+100)[1:]
                    """line = f'{file.stem}\t{log.remote_host}\t' \
                           f'{log.headers_in["User-Agent"]}\t{log.request_time}\n'"""
                    line = f"{domain}\t"
                    line += f"{str(log.remote_host).replace(D, '    ')}\t"
                    line += f"{str(log.headers_in['User-Agent']).replace(D, '    ')}\t"
                    line += f"{str(log.request_time)[:10].replace(D, '    ')}\n"
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
                        logger.info("Complete start / stop")
                        for line in this_file_write_cache:
                            fa.write(line)
                    else:
                        logger.error("XXX Incomplete start / stop XXX")
                


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