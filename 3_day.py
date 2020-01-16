print("*"*5+"1.List Comprehension One"+"*"*5)

def use_list_comprehension_one():
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 3, 1]
    print("Our original list is: ", list_one)
    # if number is odd then square that number,else multiply by 2
    modified_list = [x*x if x % 2 != 0 else x*2 for x in list_one]
    print("Modified list is: ", modified_list)
    print("Odd numbers got squared and even numbers mulitplied by 2")
    return

use_list_comprehension_one()
print()

print("*"*5+"2.List Comprehension Two"+"*"*5)

def use_list_comprehension_two():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Our original list is: ", numbers)
    # we can't use elif in list comprehension
    # if number is greater than equal to 2 and less than 5 then multiplied by 2,i.e 3,4
    #
    numbers_modified = [x*2 if (x >= 2 and x < 5) else x *
                        3 if(x >= 5 and x < 4)else x*4 for x in numbers]
    print("Modified list is:", numbers_modified)
    return

use_list_comprehension_two()
print()

print("*"*5+"3.List Comprehension Three"+"*"*5)

def use_list_comprehension_three():
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 3, 11, 12, 13, 14, 15]
    print("Original list is: ", list_one)
    modified_list = [x*x if (x % 2 != 0 and x > 9) else x*2 for x in list_one]
    print("If number is odd and greater than 9 then squared the number else multiplied by 2")
    print("Modified list is: ", modified_list)
    return

use_list_comprehension_three()
print()

print("*"*5+"4.List Comprehension Four"+"*"*5)

def use_list_comprehension_four():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Our original list is: ", numbers)
    print("Getting even numbers from the list")
    # if number mod division with 2 is 0 then number is even
    numbers_even = [x for x in numbers if x % 2 == 0]
    print("Our even numbers list is: ", numbers_even)
    return

use_list_comprehension_four()
print()

print("*"*5+"5.List Comprehension Five"+"*"*5)

def use_list_comprehension_five():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list is: ", numbers)
    print("Adding 2 to each element of list")
    numbers_sum = [x+2 for x in numbers]
    print("Modified list is: ", numbers_sum)
    return

use_list_comprehension_five()
print()

print("*"*5+"6.List Comprehension Six"+"*"*5)

def use_list_comprehension_six():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("original list is: ", numbers)
    print("Squaring numbers in list")
    numbers_square = [x*x for x in numbers]
    print("Modified list is: ", numbers_square)
    return

use_list_comprehension_six()
print()

print("*"*5+"7.List Comprehension Seven"+"*"*5)

def use_list_comprehension_seven():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list is: ", numbers)
    print("Only squaring odd numbers in list")
    odd_numbers_square = [x*x for x in numbers if x % 2 != 0]
    print("Odd numbers square:", odd_numbers_square)
    return

use_list_comprehension_seven()
print()

print("*"*5+"8.List Comprehension Eight"+"*"*5)

def use_list_comprehension_eight():
    # printing only characters in string using list comprehension
    string = "My name is Tom"
    print("Original string is: ", string)
    print("Using list comprehension:")
    new_string = "".join([item for sublist in string.split()
                          for item in sublist])
    print(new_string)
    for char in new_string:
        print(char)
    return

use_list_comprehension_eight()
print()

print("*"*5+"9.List Comprehension Nine"+"*"*5)

def use_list_comprehension_nine():
    # printing only characters in string using list comprehension
    string = "My name is Tom"
    print("Original string is: ", string)
    print("Use of list comprehension one line code")
    for i in "".join([item for sublist in string.split() for item in sublist]):
        print(i)
    return

use_list_comprehension_nine()
print()

print("*"*5+"10.List Comprehension Ten"+"*"*5)

def use_list_comprehension_ten():
    # addition of two lists
    numbers_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_two = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
    print("Our first list is: ", numbers_one)
    print("Our second list is: ", numbers_two)
    print("Adding two lists without list comprehension")
    sum_three = []
    for i in range(len(numbers_one)):
        sum_three.append(numbers_one[i]+numbers_two[i])
    print("Addition of two list is: ", sum_three)
    print("Using list comprehension")
    sum_three = [numbers_one[i]+numbers_two[i]
                 for i in range(len(numbers_two))]
    print("Addition of two list is: ", sum_three)
    return

use_list_comprehension_ten()
print()

print("*"*5+"11.List Comprehension Eleven"+"*"*5)

def use_list_comprehension_eleven():
    numbers_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Our original list is: ", numbers_one)
    print("Solving without list comprehension")
    number_divisible_five = []
    for number in numbers_one:
        if number % 5 == 0:
            number_divisible_five.append(number)
    print("Numbers divisible five in list:", number_divisible_five)
    print("Using List Comprehension")
    number_divisible_five = [
        number for number in numbers_one if number % 5 == 0]
    print("Numbers divisible five in list:", number_divisible_five)
    return

use_list_comprehension_eleven()
print()

print("*"*5+"12.List Comprehension Twelve"+"*"*5)

def use_list_comprehension_twelve():
    # finding length of each word in string except "the"
    sentence = "My name is Mosh, I am the author"
    print("Our original string is: ", sentence)
    print("Solution without using list comprehension")
    length_list = []
    for word in sentence.split():
        if word.lower() == "the":
            continue
        length_list.append(len(word))
    print("Lengths of words in list excluding \"the\" length", length_list)

    print("Using List Comprehension")
    length_list = [len(word)
                   for word in sentence.split() if word.lower() != "the"]
    print("Lengths of words in list excluding \"the\" length", length_list)
    return

use_list_comprehension_twelve()
print()

print("*"*5+"13.List Comprehension Thirteen"+"*"*5)

def use_list_comprehension_thirteen():
    # finding list of vowels in string
    string = "what is your name"
    print("Our original string is: ", string)
    vowels_list = []
    print("Solution without using list comprehension")
    for alpha in string:
        if alpha == "a" or alpha == "e" or alpha == "i" or alpha == "o" or alpha == "u":
            if alpha not in vowels_list:
                vowels_list.append(alpha)
    print("Vowels in string:", vowels_list)
    print("Using List Comprehension")
    vowels_list = list(set([alpha for alpha in string if alpha == "a" or alpha ==
                            "e" or alpha == "i" or alpha == "o" or alpha == "u"]))
    print("Vowels in string:", vowels_list)
    return

use_list_comprehension_thirteen()
print()

print("*"*5+"14.List Comprehension Fourteen"+"*"*5)

def use_list_comprehension_fourteen():
    # remove all vowels in string
    string = "what is your name"
    print("Our original string is: ", string)
    print("Solution without using list comprehension")
    consonant_list = []
    for alpha in string:
        if alpha == "a" or alpha == "e" or alpha == "i" or alpha == "o" or alpha == "u" or alpha == " ":
            continue
        else:
            consonant_list.append(alpha)
    print("String alphabets without vowels:", consonant_list)
    print("Using List Comprehension")
    consonant_list = [alpha for alpha in string if alpha != "a" and alpha !=
                      "e" and alpha != "i" and alpha != "o" and alpha != "u" and alpha != " "]
    print("String alphabets without vowels:", consonant_list)
    return

use_list_comprehension_fourteen()
print()

print("*"*5+"15.Loop With Else"+"*"*5)

def loop_with_else():
    for number in range(10):
        print(number)
    else:
        print("Done")
    # above code , no loop break so else got executed
    print("For with break")
    for number in range(10):
        print(number)
        if number > 5:
            break
        # print(number)
        # if break got executed else will not get executed
    else:
        print("Done")
    return

loop_with_else()
print()

print("*"*5+"16.Use break and continue"+"*"*5)

def use_break_and_continue():
    command = input("Please enter your command ")

    while(command):
        if command.lower() == "end":
            break
        else:
            command = input("Please enter your command ")
            continue

    print("You are out of the loop")
    return

use_break_and_continue()
print()

print("*"*5+"17.Use continue"+"*"*5)

def use_continue():
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 3, 1]
    print("Our original list is: ", list_one)
    print("Numbers greater than 5 are: ")
    # continue statement skips current loop iteration and goes for next iteration
    for number in list_one:
        if(number < 5):
            continue
        print(number)
    return

use_continue()
print()

print("*"*5+"18.Iterating Over Two Lists"+"*"*5)

def iterating_over_two_list():
    # iterate over two list and observe output according to conditions
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_two = [11, 12, 13, 14, 15, 16, 17, 18, 19, 101]
    for lst in list_one:
        for i in list_two:
            if (i > 15):
                break
            print(lst, i)
        if(lst > 5):
            break
    print("Another approach")
    for lst in list_one:
        for i in list_two:
            if (i > 15):
                break
            print(lst, i)
        break
    return

iterating_over_two_list()
print()
