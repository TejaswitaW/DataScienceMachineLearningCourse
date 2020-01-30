from concurrent.futures import ThreadPoolExecutor
import time


def task(message):
    time.sleep(2)
    return message


def main():
    # we can specify max_workers value,default is 5
    executor = ThreadPoolExecutor(max_workers=10)
    future = executor.submit(task, ("Completed"))
    # future object contains status of threads
    while future.done() == False:
        time.sleep(1)
    print("Done!!!!")
    print(future.result())


if __name__ == "__main__":
    main()
