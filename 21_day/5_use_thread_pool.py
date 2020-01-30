from concurrent.futures import ThreadPoolExecutor
import time
import threading as tr


def task(message):
    time.sleep(2)
    print("Thread name is: ", tr.current_thread())
    print(message)


def main():
    executor = ThreadPoolExecutor(max_workers=5)
    for i in range(10):
        future = executor.submit(task, "Completed {}".format(i))


if __name__ == "__main__":
    main()
"""
Output is in following format for all threads:
Thread name is:  <Thread(ThreadPoolExecutor-0_1, started daemon 3228)>
Completed 1
"""
