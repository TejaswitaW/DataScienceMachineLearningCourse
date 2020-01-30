import threading as tr
import time


def sleeper(n, name):
    print("Hi, I am {} going to sleep for 5 seconds\n".format(name))
    # cpu sleeps for 5 seconds,so main thread will start execution
    time.sleep(n)
    print("{} has woken from sleep\n".format(name))


# sleep_thread is created for sleeper function
sleep_thread = tr.Thread(target=sleeper, name="Thread1", args=(5, "Thread1"))
# sleep_thread starts its execution when we start it
sleep_thread.start()
# as cpu sleeps for 5 seconds , main thread executed following statement
# observe the final output
print("Hi")
"""
Output is:
Hi, I am Thread1 going to sleep for 5 seconds

Hi
Thread1 has woken from sleep
"""
