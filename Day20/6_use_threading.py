import threading as tr
var_x = 0


def increment():
    global var_x
    var_x += 1


def thread_task(lock):
    for number in range(1000000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global var_x
    var_x = 0
    # creating lock
    lock = tr.Lock()
    thread_one = tr.Thread(target=thread_task, args=(lock,))
    thread_two = tr.Thread(target=thread_task, args=(lock,))
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()


# two threads using same resource
# so need to use lock
if __name__ == "__main__":
    for number in range(10):
        main_task()
        print("Iteration{0}:x={1}".format(number, var_x))
