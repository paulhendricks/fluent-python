#!/usr/bin/python3
"""TO BE EDITED

Not Complete!
"""
from concurrent import futures
import time


def wait(x):
    print("Waiting!")
    time.sleep(x)
    print("Done waiting!")
    return True


def main_thread():
    times = [1, 1, 1, 1]
    executor = futures.ThreadPoolExecutor
    results = executor.map(wait, times)
    return len(list(results))


def main_process():
    times = [1, 1, 1, 1]
    with futures.ProcessPoolExecutor as executor:
        res = executor.map(wait, times)
    return len(list(res))


if __name__ == '__main__':
    print("Started!")
    main_thread()
    print("Finished!")
