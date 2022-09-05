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


logger.add("./apachexvt_{time}.log")
INPUT_PATH = '/Users/andy/ws/lessons/data/sam/input/'
OUTPUT_PATH = "/Users/andy/ws/lessons/data/sam/output/"
DONE_PATH = "/Users/andy/ws/lessons/data/sam/done/"
OUTPUT_FILE = OUTPUT_PATH + "log_summary.csv"
RESTART_SCRIPT_FILE = OUTPUT_PATH + "move-processed-gz.sh"
START_YMD = '2021-08-01'
START_DAYS = 31
STOP_YMD = '2022-07-31'
STOP_DAYS = 31

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
def getlogs(files, ignores):
    number_processed = 0
    with open(OUTPUT_FILE, 'w') as fo:
        fo.write(f'domain{D}client{D}user_agent{D}time{N}')
    if os.path.exists(RESTART_SCRIPT_FILE):
        os.remove(RESTART_SCRIPT_FILE)
    with open(RESTART_SCRIPT_FILE, 'a') as rsf:
        rsf.write('#!/bin/bash\n')
        rsf.write('# change me to executable and run to restart without reprocessing\n')
        with open(OUTPUT_FILE, 'a') as fa:
            for file in files:
                domain = str(file)[len(INPUT_PATH):]
                domain = domain[:domain.find('/')]
                print(f"Domain {domain}: working on # {number_processed} {file}...")
                with gzip.open(file,'r') as f:
                    number_processed += 1
                    # abandon when testing
                    """if number_processed > 1000:
                        exit(1)"""
                    for log_text in f:
                        try:
                            log = parser.parse(log_text.decode())
                        except Exception as e:
                            logger.info(e)
                            continue
                        if log.status not in (303, 304, 305) and \
                                not (200 <= log.status < 300):
                            continue
                        if not (START_YMD <= str(log.request_time)[:10] <= STOP_YMD):
                            continue
                        if not ("GET" in str(log_text)):
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
                        for ignore in ignores:
                            """print("ignore data", ignore[2], mm, ignore[1], yyyy[2:],
                                  ignore[0],
                                  f"{file}")"""
                            if ignore[2] == mm and ignore[1] == yyyy[2:] and \
                                ignore[0] in str(file):
                                print("XXXignoringXXX",
                                      ignore[2], mm, ignore[1], yyyy[2:],
                                      ignore[0],
                                      f"{str(log.remote_host).replace(D, '    ')}\t")
                                continue
                        fa.write(line)

                rsf.write(f'mv {INPUT_PATH + str(file.name)} {DONE_PATH + str(file.name)}\n')


def filename_to_date(f):
    return f"{20}{f[-2:]}-{f[:2]}-{f[2:4]}"


def getfiles():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    paths = []
    start_eliminates = {}
    stop_eliminates = {}
    for filepath in Path(INPUT_PATH).rglob('*.gz'):
        if filepath.is_dir():
            continue
        file_date = filename_to_date(str(filepath)[-9:-3])
        domain = str(filepath)[len(INPUT_PATH):]
        domain = domain[domain.rfind('/')+1:-10]
        if START_YMD <= file_date <= STOP_YMD:
            print(START_YMD, file_date, STOP_YMD, (file_date[:7] == START_YMD[:7]))
            if file_date[:7] == START_YMD[:7]:
                if start_eliminates.get((domain, file_date[:7]), None) is None:
                    start_eliminates[(domain, file_date[:7])] = 1
                else:
                    start_eliminates[(domain, file_date[:7])] += 1
            if file_date[:7] == STOP_YMD[:7]:
                if stop_eliminates.get((domain, file_date[:7]), None) is None:
                    stop_eliminates[(domain, file_date[:7])] = 1
                else:
                    stop_eliminates[(domain, file_date[:7])] += 1
            paths.append(filepath)
    print(start_eliminates)
    print(start_eliminates)
    ignores = []
    for key, value in start_eliminates.items():
        if value != START_DAYS:
            print((key[0], key[1][2:4], key[1][-2:], value))
            ignores.append((key[0], key[1][2:4], key[1][-2:], value))
    for key, value in stop_eliminates.items():
        if value != STOP_DAYS:
            print((key[0], key[1][2:4], key[1][-2:], value))
            ignores.append((key[0], key[1][2:4][:2], key[1][-2:], value))

    return paths, ignores


def main():
    all_logs, ignores = getfiles()
    getlogs(all_logs, ignores)
    

if __name__ == "__main__":
    main()
