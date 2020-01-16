print("*"*5+"1.Find Smallest Number in List"+"*"*5)


def find_smallest_number_in_list():
    numbers = [1, 2, 3, -1000, 4, 5, -1, 7, -7, 0, -100]
    print("Our original list is: ", numbers)
    min_number = numbers[0]
    for value in range(len(numbers)):
        if(numbers[value] < min_number):
            min_number = numbers[value]
    print("Minimum number from list is:", min_number)
    return


find_smallest_number_in_list()
print()
print("*"*5+"2.Dictionary of Numbers with Count"+"*"*5)


def dictionary_of_numbers_with_count():
    numbers_list = [1, 3, 77, 888, 33, 77, 33, 33, 888, 1, 2, 5, 1, 888]
    numbers_dict = {}
    print("Our original list is: ", numbers_list)
    for number in numbers_list:
        if number in numbers_dict:
            numbers_dict[number] += 1
        else:
            numbers_dict[number] = 1
    print("Our dictionary of numbers with count is:", numbers_dict)
    return


dictionary_of_numbers_with_count()
print()
print("*"*5+"3.Printing Squares of Numbers"+"*"*5)


def squares_of_numbers():
    number = int(input("Enter number "))
    for num in range(1, number):
        square = num*num
        print("Square of", num, "is", square)
    return


squares_of_numbers()
print()

print("*"*5+"4.Printing Strings Lengths"+"*"*5)


def printing_string_length():
    names_string = ["Tom", "Mosh", "Charlie", "Leonardo", "Andrew Ng"]
    print("Our list of names is: ", names_string)
    for name in names_string:
        print("Length of" + " " + name + " is", len(name))
    return


printing_string_length()
print()

print("*"*5+"5.Subtract Numbers in Two Lists"+"*"*5)


def subtract_numbers_in_two_lists():
    list_one = [1, 2, 3, 4, 5, 6]
    list_two = [11, 12, 13, 14, 15, 16]
    list_three = []
    print("List one is: ", list_one)
    print("List two is: ", list_two)
    for value in range(len(list_one)):
        number = list_two[value]-list_one[value]
        list_three.append(number)
    print("Our new list after subtraction of elements from two list is:", list_three)
    return


subtract_numbers_in_two_lists()
print()

print("*"*5+"6.Operations on List Numbers"+"*"*5)


def operations_list_numbers():
    list_num = [1, 2, 3, 4, 5]
    print("Our original list is: ", list_num)
    sum = 0
    for value in range(len(list_num)):
        sum = sum+list_num[value]
    print("Sum of numbers in list is:", sum)
    print("Average of numbers:", sum/len(list_num))
    print("Swapping of list element")
    temp = list_num[0]
    list_num[0] = list_num[len(list_num)-1]
    list_num[len(list_num)-1] = temp
    print("After swapping first element with last element our list becomes:", list_num)
    return


operations_list_numbers()
print()

print("*"*5+"7.Take Input From User Till Enter \"end\""+" *"*5)


def take_input_till_user_enter_end():
    command = input("Please enter your command ")
    while(command.lower() != "end"):
        print("Your entered command: ", command)
        command = input("Please enter your command ")
    print("You are out of the loop")
    return


take_input_till_user_enter_end()
print()
