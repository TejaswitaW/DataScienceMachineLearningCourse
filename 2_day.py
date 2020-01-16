print("*"*5+"1.Compare Two Dictionaries"+"*"*5)


def compare_two_dict():
    dict_one = {"name": "Tom", "city": "New York", "age": 25, "salary": 100000}
    dict_two = {"name": "Mosh", "city": "New York",
                "age": 35, "salary": 200000}
    print("Our dictionary one is: ", dict_one)
    print("Our dictionary two is: ", dict_two)
    # comparing two dictionaries values and printing values those are different
    print("After comparing two dictionary values,different values are:")
    for key in dict_one.keys():
        if dict_one[key] != dict_two[key]:
            print("Key is ", key, dict_one[key])
            print("Key is ", key, dict_two[key])
    return


compare_two_dict()
print()

print("*"*5+"2.Merge Two Dictionaries"+"*"*5)


def merge_two_dict_first():
    dict_numbers_one = {"a": 1, "b": 2, "c": 3, "d": 5, "e": 10}
    dict_numbers_two = {"f": 111, "g": 222, "h": 333, "i": 555, "j": 1000}
    merged_dict = {}
    print("Our first dictionary is: ", dict_numbers_one)
    print("Our second dictionary is: ", dict_numbers_two)
    # merging two dictionaries in third dictionary
    for key, value in dict_numbers_one.items():
        merged_dict[key] = value
    for key, value in dict_numbers_two.items():
        merged_dict[key] = value
    print("Our merged dictionary is: ", merged_dict)
    return


merge_two_dict_first()
print()


def merge_two_dict_second():
    dict_numbers_one = {"a": 1, "b": 2, "c": 3, "d": 5, "e": 10}
    dict_numbers_two = {"f": 111, "g": 222, "h": 333, "i": 555, "j": 1000}
    # merging one dictionary in another dictionary
    for key, value in dict_numbers_one.items():
        dict_numbers_two[key] = value
    print("After merging dictionaries:", dict_numbers_two)
    return


merge_two_dict_second()
print()

print("*"*5+"3.Sepearating Odd Even Numbers from List"+"*"*5)


def odd_even_numbers_from_list():
    numbers_list = [1, 11, 22, 12, 13, 14, 77, 43, 89, 91, 80, 123, 543]
    odd_numbers_list = []
    even_numbers_list = []
    # if number's mod division with 2 is equal to 0 then number is even,
    # otherwise number is odd
    for number in numbers_list:
        if number % 2 == 0:
            even_numbers_list.append(number)
        else:
            odd_numbers_list.append(number)
    print("Original numbers list is: ", numbers_list)
    print("Even numbers list is: ", even_numbers_list)
    print("Odd numbers list is: ", odd_numbers_list)
    return


odd_even_numbers_from_list()
print()

print("*"*5+"4.Sepearating Odd Even Numbers from Dictionary"+"*"*5)


def odd_even_numbers_from_dict():
    dict_numbers = {"a": 1, "b": 2, "c": 3, "d": 5, "e": 10}
    odd_numbers_dict = {}
    even_numbers_dict = {}
    # if number's mod division with 2 is equal to 0 then number is even,
    # otherwise number is odd
    for key, value in dict_numbers.items():
        if value % 2 == 0:
            even_numbers_dict[key] = value
        else:
            odd_numbers_dict[key] = value
    print("Our original dictionary is: ", dict_numbers)
    print("Odd numbers dictionary is: ", odd_numbers_dict)
    print("Even numbers dictionary is: ", even_numbers_dict)
    return


odd_even_numbers_from_dict()
print()

print("*"*5+"5.Printing Prime Numbers From Given Range"+"*"*5)


def printing_prime_numbers_in_given_range():
    start = int(input("Enter start of your range: "))
    end = int(input("Enter end of your range: "))
    print("Prime numbers in given range {0} and {1} are:".format(start, end))
    # prime number have only two factors 1 and number itself
    for number in range(start, end+1):
        if number > 1:
            for value in range(2, number):
                if number % value == 0:
                    break
            else:
                print(number)
    return


printing_prime_numbers_in_given_range()
print()

print("*"*5+"6.Printing Numbers Triangle Pattern"+"*"*5)


def printing_numbers_in_trianlge_pattern():
    """
                1
            2       3
        4       5       6
    7       8       9       10
    """
    rows = int(input("Enter rows number "))
    num = 1
    # outer loop is for rows
    # inner loop is for changing value to be printed
    for row in range(rows):
        print(" "*(rows-row-1), end="")
        for j in range(row+1):
            print(num, end=" ")
            num += 1
        print()
    return


printing_numbers_in_trianlge_pattern()
print()

print("*"*5+"7.Second Largest Element From Dictionary"+"*"*5)


def second_largest_element_from_dictinary():
    dict_numbers = {"1": 10, "2": 13, "3": 7, "4": 5, "5": 15, "6": 14}
    print("Original dictionary is: ", dict_numbers)
    print(dict_numbers.values())
    max = 0
    second_max = 0
    for key in dict_numbers.keys():
        if dict_numbers[key] > max:
            max = dict_numbers[key]
        # when number is less than maximum then it is second maximum number
        if dict_numbers[key] > second_max and dict_numbers[key] < max:
            second_max = dict_numbers[key]
    print("Second max is:", second_max)
    return


second_largest_element_from_dictinary()
print()

print("*"*5+"8.Sum of Dictionary Values"+"*"*5)


def sum_of_dictionary_values():
    dict_numbers = {"a": 1, "b": 2, "c": 3, "d": 5, "e": 10}
    print("Our original dictionary is: ", dict_numbers)
    sum = 0
    # using values() function on dictionary got values,
    # and then did sum
    for value in dict_numbers.values():
        sum += value
    print("Sum of values in dictionary is:", sum)
    return


sum_of_dictionary_values()
print()
