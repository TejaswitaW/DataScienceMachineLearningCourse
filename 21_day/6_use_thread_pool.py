"""
We will learn use of executor.map().
It is widely used in case, when we want to apply a certain function,
to every element within iterables. 
"""
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
# list
values = [2, 3, 4, 5]


def square(n):
    return n**2


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        # applying square function on every element in list
        # returns generator object
        results = executor.map(square, values)
        # print(results)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

"""
Output is:
4
9
16
25
"""
