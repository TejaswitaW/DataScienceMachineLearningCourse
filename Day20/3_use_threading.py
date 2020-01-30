import threading as tr
import time
total = 4


def creates_items():
    global total
    for number in range(10):
        time.sleep(2)
        print("Added Item")
        total += 1
    print("Creation is done")


def creates_items_2():
    global total
    for number in range(7):
        time.sleep(1)
        print("Added Item")
        total += 1
    print("Creation is done")


def limits_items():
    global total
    while True:
        if total > 5:
            print("Overload")
            total -= 3
            print("Subtracted 3")
        else:
            time.sleep(1)
            print("Waiting")


thread_one = tr.Thread(target=creates_items, name="Thread1")
thread_two = tr.Thread(target=creates_items_2, name="Thread1")
thread_three = tr.Thread(target=limits_items, name="Thread1")
thread_one.start()
thread_two.start()
thread_three.start()
thread_one.join()
thread_two.join()
thread_three.join()
print("Our ending value of total is: ", total)
# observe the output
# ouput does not reach to last print statement
# this is because of infinite for loop
# but our need is thread_three should stop after main thread execution
