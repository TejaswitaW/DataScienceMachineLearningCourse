import threading as tr
var_x = 0


def increment():
    global var_x
    var_x += 1


def thread_task():
    for number in range(1000000):
        increment()


def main_task():
    global var_x
    var_x = 0
    thread_one = tr.Thread(target=thread_task)
    thread_two = tr.Thread(target=thread_task)
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()


# two threads using same resource
# we did not use lock so we get incorrect output
if __name__ == "__main__":
    for number in range(10):
        main_task()
        print("Iteration{0}:x={1}".format(number, var_x))
