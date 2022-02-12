if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
        print("Use Threads")
else:
    print("Multi Processing")

"""
    Is it IO-BOUND ? ---------> USE asyncio
    IS IT CPU-HEAVY ? -----> USE multiprocessing
    ELSE ? ----------------------> USE threading
So basically stick to threading unless you have IO/CPU problems.
EXCELLENT article:
https://leimao.github.io/blog/Python-Concurrency-High-Level/
"""
