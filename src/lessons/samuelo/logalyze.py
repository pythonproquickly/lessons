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
log_format = "%h %l %u %t \"%r\" %s %b \"%{Referer}i\" \"%{User-agent}i\" %D"
parser = LogParser(log_format)
analysis = []

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
                        continue
                    yyyy = str(log.request_time.year)
                    mm = str(log.request_time.month+100)[1:]
                    dd = str(log.request_time.day+100)[1:]
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


def getfiles():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    paths = []
    for filepath in Path(PATH).rglob('*'):
        paths.append(filepath)
    return paths


def main():
    all_logs = getfiles()
    getlogs(all_logs)
    

if __name__ == "__main__":
    main()