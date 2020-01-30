"""
Creating thread pool is preferred over instantiating new threads for every task,
when we need to do large number of tasks.
"""
from concurrent.futures import ThreadPoolExecutor
import time


def task(message):
    time.sleep(2)
    return message


def main():
    # creating pool of threads,default value of number of threads is 5
    # creating object of ThreadPoolExecutor
    executor = ThreadPoolExecutor()
    # submitting task to thread pool
    # returns future object
    future = executor.submit(task, ("Completed"))
    # print(type(future))#<class 'concurrent.futures._base.Future'>
    # future object has method called done()
    # which tells task finished or not
    print(future.done())
    # waits to complete task
    time.sleep(2)
    print(future.done())
    print(future.result())


if __name__ == "__main__":
    main()
