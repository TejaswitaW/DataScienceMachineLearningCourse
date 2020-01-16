print("*"*5+"1.Binary Search"+"*"*5)


def binary_search():
    numbers_list = [11, 2, 12, 34, 56, 76, 3, 0, 4, 7, 8, 100, 1, 1000, -89]
    # first we need to sort this data in ascending order
    print("our original list is: ", numbers_list)
    numbers_list.sort()
    print("After sorting the list is: ", numbers_list)
    key = int(input("Enter key to be searched: "))
    low = 0
    # high gives highest index of list element
    high = len(numbers_list)-1
    while(low <= high):
        middle = (low+high)//2
        # key is always compared with middle element
        if numbers_list[middle] == key:
            print("Key found at index: ", middle)
            break
        # if key is less than middle element,second half of list is discarded
        elif numbers_list[middle] > key:
            high = middle-1
        # if key is greater than middle element,first half of list is discarded
        elif numbers_list[middle] < key:
            low = middle+1
        # if key not found in list then else part will get executed
    else:
        print("Key is not present in the list")
    return


binary_search()
print()

print("*"*5+"2.Extracting Dictionary Values Using List Comprehension"+"*"*5)


def dictionary_values_using_list_comprehension():
    dict_one = {"name": "Mosh", "age": 35, "salary": 200000}
    # traversing dictionary using key and getting dictionary values
    print("Using dict.keys() function")
    dict_values = [dict_one[key] for key in dict_one.keys()]
    print("Values in dictionary", dict_values)
    # traversing dictionary values and getting dictionary values
    print("Using dict.values() function")
    dict_values = [value for value in dict_one.values()]
    print("Values in dictionary", dict_values)
    return


dictionary_values_using_list_comprehension()
print()

print("*"*5+"3.Use of List Comprehension"+"*"*5)


def use_list_comprehension():
    # input is: a = [[1], [2], [3]]
    # output is: b = [1,2,3]
    print("First approach using loop,using append method")
    a = [[1], [2], [3]]
    b = []
    for item in a:
        for i in item:
            b.append(i)
    print(b)
    print("Second approach, using extend method")
    a = [[1], [2], [3]]
    b = []
    for item in a:
        b.extend(item)
    print(b)
    print("Third approach,using list comprehension")
    b = [i for item in a for i in item]
    print(b)
    return


use_list_comprehension()
print()

print("*"*5+"4.Function Introduction"+"*"*5)


def function_introduction():
    # add function takes two arguments and return sum of these two numbers
    def add(val_one, val_two):
        sum = val_one+val_two
        return sum
    value_one = int(input("Enter first value "))
    value_two = int(input("Enter second value "))
    summation = add(value_one, value_two)
    print("Summation of two numbers is: ", summation)
    return


function_introduction()
print()

print("*"*5+"5.Function With Default Arguments"+"*"*5)


def function_with_default_arguments():
    # add function takes two arguments and return sum of these two numbers
    # we are using default arguments in funciton
    def add_val(val_one=10, val_two=100):
        sum = val_one+val_two
        return sum
    summation = add_val(100)
    print("Summation of two numbers is: ", summation)
    summation = add_val()
    print("Summation of two numbers is: ", summation)
    summation = add_val(10, 10)
    print("Summation of two numbers is: ", summation)
    return


function_with_default_arguments()
print()
