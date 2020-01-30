from concurrent.futures import ThreadPoolExecutor
import time


def task(message):
    time.sleep(2)
    print(message)


def main():
    executor = ThreadPoolExecutor(max_workers=5)
    #executor = ThreadPoolExecutor(max_workers=1)
    future = executor.submit(task, ("Completed"))
    future = executor.submit(task, ("Completed_one"))
    future = executor.submit(task, ("Completed_two"))
    future = executor.submit(task, ("Completed_three"))
    future = executor.submit(task, ("Completed_four"))
    # future contains status of threads
    while future.done() == False:
        time.sleep(1)
    print("Done")
    # print(future.result())
    # print(type(future.result()))


if __name__ == "__main__":
    main()
