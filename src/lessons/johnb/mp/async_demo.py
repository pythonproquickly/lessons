import asyncio
import time
import datetime


async def c(delay, s):
    await asyncio.sleep(delay)
    print(s)


async def main():
    taskA = asyncio.create_task(c(3, "start first, finished when?"))
    taskB = asyncio.create_task(c(2, "start second, finishes when?"))

    print(f'started at {datetime.datetime.strptime(time.ctime(),"%c")}')

    await taskA
    await taskB

    print(f'stopped at {datetime.datetime.strptime(time.ctime(),"%c")}')


asyncio.run(main())
