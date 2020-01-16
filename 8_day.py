from functools import reduce
print("*"*5+"1.Filter Method"+"*"*5)
def using_filter_method_get_even_numbers_from_list():
    #filter_even_number method filtering the numbers,
    #in list according to condition
    """
    This method gives us the even numbers in the list.
    """
    def filter_even_number(number):
        if number % 2 == 0:
            return number


    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print("Originl number list is: ",numbers_list)
    filtered_list = list(filter(filter_even_number, numbers_list))
    print("List with only even numbers is: ",filtered_list)
    return
using_filter_method_get_even_numbers_from_list()
print()

def use_filter_method_get_numbers_greater_than_70():
    """
    This method gives the numbers in list which are greater than 70.
    """
    def my_filter_fun(number):
        if number > 70:
            return True


    scores = [30, 50, 60, 70, 80, 90, 20, 54, 98, 77, 66, 75]
    print("Our original list is: ",scores)
    filtered_list = list(filter(my_filter_fun, scores))
    print("Numbers in list which are greater than 70: ",filtered_list)
    return
use_filter_method_get_numbers_greater_than_70()
print()

print("*"*5+"2.Map Method"+"*"*5)
def use_map_method_one():
    """
    This method map list elements to operation_map method.
    operation_map method mulitplies even number with 3 and odd number with 5.
    """
    def operation_map(number):
        if number % 2 == 0:
            return number*3
        else:
            return number*5


    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print("Our original list of numbers is: ",numbers_list)
    modified_list = list(map(operation_map, numbers_list))
    print("Our modified list is: ",modified_list)
    return
use_map_method_one()
print()

def use_map_method_two():
    """
    This method maps string to string_operation_map function.
    string_operation_map function, appends words with length greater that 6 with "The".
    """
    def string_operation_map(word):
        if len(word) > 6:  # try with filter use
            return "The "+word
        else:
            return word


    string = "python decorator wraps another function"
    print("Our original string is: ",string)

    # print(string.split())
    modified_string = " ".join(
        list(map(string_operation_map, string.split())))
    print("Our modified string is: ",modified_string)
    return
use_map_method_two()
print()

def use_map_method_three():
    """
    This function converts pet names list to uppercase names
    """
    my_pets = ["cat", "dog", "parrot", "rabbit"]
    print("Our original list is: ",my_pets)
    my_pets_upper = []
    for pet in my_pets:
        my_pets_upper.append(pet.upper())
    print(my_pets_upper)


    def my_map(string):
        return string.upper()


    print("First approach")
    #used user defined function my_map
    my_pets_upper_two = list(map(my_map, my_pets))
    print(my_pets_upper_two)
    print("Second approach")
    #used built_in string function str.upper
    my_pets_upper_two = list(map(str.upper, my_pets))
    print(my_pets_upper_two)
    print("Third approach")
    my_pets_upper_two = map(str.upper, my_pets)
    for name in my_pets_upper_two:
        print("Name of pet is:", name)
    return
use_map_method_three()
print()

def use_map_method_four():
    """
    This function multiply numbers in list with their index.
    """
    def index_multiply(number, index):
        return number*index


    list_one = [1, 2, 3, 4, 5, 6]
    print("Our original list is: ",list_one)
    index_mul_list = list(map(index_multiply, list_one, range(len(list_one))))
    print("Our modified list is: ",index_mul_list)
    # print(type(range(7)))
    # print(range(7))
    return
use_map_method_four()
print()

def use_map_method_five():
    """
    This function adds numbers in two different lists.
    """
    def add_function(number_one, number_two):
        return number_one+number_two


    list_one = [1, 2, 3, 4, 5, 6]
    list_two = [10, 20, 30, 40, 50, 60]
    print("Our list one is: ",list_one)
    print("Our list two is: ",list_two)
    added_numbers = list(map(add_function, list_one, list_two))
    print("After addition of numbers in two lists: ",added_numbers)
    return
use_map_method_five()
print()

print("*"*5+"3.Reduce Method"+"*"*5)
def use_reduce_method():
    """
    This function adds all numbers in list.
    """
    def do_sum(number_one, number_two):
        return number_one+number_two

    numbers_list = [1, 2, 3, 4, 5]
    print("Our original list is: ",numbers_list)
    # add with initial value 100
    result = reduce(do_sum,numbers_list, 100)
    print("Sum of all numbers in the list with initial value 100: ",result)
    return
use_reduce_method()
print()

def use_reduce_method_one():
    """
    This function converts list of words in string.
    """
    words_list = ["My", "name", "is", "Tom"]

    print("Our original list of words is: ",words_list)
    def my_fun(word_one, word_two):
        return word_one+" "+word_two


    new_list = reduce(my_fun, words_list)
    print("We got string: ",new_list)
    return
use_reduce_method_one()
print()
