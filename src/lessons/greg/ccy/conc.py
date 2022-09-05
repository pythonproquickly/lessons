import functools
import time
import threading
import requests
import multiprocessing
import aiohttp
import asyncio


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # also time.process_time()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Ran {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def workload():
    return 10


def do_some_work_that_blocks_for_duration():
    time.sleep(workload())


async def a_do_some_work_that_blocks_for_duration():
    await asyncio.sleep(workload())
    # do_some_work_that_blocks_for_duration()


def jobs():
    return 5


def web_workload():
    return (
        "https://www.propertyinsurancecoveragelaw.com/files/files/Reference%20Manual%20on%20Scientific%20Evidence.pdf",
        "https://redhawk.concurrent-rt.com/docs/root/2PowerMAX/PLDE/zarchive/C/0890497-030.pdf",
        "https://machmotion.com/documentation/Software/Mach4/Mach4-G-and-M-Code-Reference-Manual.pdf",
        "https://www.st.com/resource/en/reference_manual/CD00246267-.pdf",
        "https://docs.oracle.com/cd/E19641-01/802-1948/802-1948.pdf",
        "https://www.vmware.com/pdf/ws6_manual.pdf",
        "https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_archives/PDFReference.pdf",
        "http://h10032.www1.hp.com/ctg/Manual/c03730648.pdf",
        "http://public.dhe.ibm.com/systems/power/docs/systemi/v6r1/en_US/sc415445.pdf",
    )


@timer
def single_thread_best():
    for _ in range(jobs()):
        do_some_work_that_blocks_for_duration()


@timer
def single_thread_representative():
    urls = web_workload()
    for url in urls:
        r = requests.get(url)


@timer
def multi_thread_best():
    threads = []
    for _ in range(jobs()):
        th = threading.Thread(target=do_some_work_that_blocks_for_duration)
        threads.append(th)
        th.start()

    for index, thread in enumerate(threads):
        thread.join()


@timer
def multi_thread_representative():
    threads = []
    for url in web_workload():
        th = threading.Thread(target=requests.get,
                              args=(url,))
        threads.append(th)
        th.start()

    for index, thread in enumerate(threads):
        thread.join()


@timer
def multi_process_best():
    processes = []
    for _ in range(jobs()):
        processes.append(multiprocessing.Process(
            target=do_some_work_that_blocks_for_duration))
        processes[-1].start()
    for process in processes:
        process.join()


@timer
def multi_process_representative():
    processes = []
    for url in web_workload():
        processes.append(multiprocessing.Process(target=requests.get,
                                                 args=(url,)))
        processes[-1].start()
    for process in processes:
        process.join()


# note decorator doesn't work in async functions... Find out why
async def async_process_best():
    start_time = time.perf_counter()  # also time.process_time()
    crs = [a_do_some_work_that_blocks_for_duration() for _ in range(jobs())]
    await asyncio.gather(*crs)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Ran async_process_best in {run_time:.4f} secs")


# note decorator doesn't work in async functions... Find out why
async def async_process_representative():
    start_time = time.perf_counter()  # also time.process_time()
    async with aiohttp.ClientSession() as session:
        for url in web_workload():
            async with session.get(url) as response:
                await response.read()
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Ran async_process_representative in {run_time:.4f} secs")


async def main():
    print(f"With total blocking, best case is {workload()}, worst case is "
          f"{jobs() * workload()}")

    single_thread_best()
    multi_thread_best()
    multi_process_best()
    await async_process_best()
    single_thread_representative()
    multi_thread_representative()
    multi_process_representative()
    await async_process_representative()


if __name__ == "__main__":
    asyncio.run(main())
