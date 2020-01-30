from concurrent.futures import ThreadPoolExecutor
import time


def task(message):
    time.sleep(2)
    print(message)


def main():
    executor = ThreadPoolExecutor(max_workers=5)
    for sr_no in range(10):
        future = executor.submit(task, "Completed {}".format(sr_no))


if __name__ == "__main__":
    main()
