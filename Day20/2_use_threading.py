import threading as tr
import time


def print_cube(number):
    print("Cube:{}".format(number**3))


def print_square(number):
    print("Square:{}".format(number**2))


if __name__ == "__main__":
    # two threads are created
    thread_one = tr.Thread(target=print_cube, args=(10,))
    thread_two = tr.Thread(target=print_square, args=(10,))
    # threads start
    thread_one.start()
    thread_two.start()

    # wait until thread_one is completely executed
    thread_one.join()
    # wait until thread_one is completely executed
    thread_two.join()

    # both threads completely exectued
    print("Done")
