print("*"*5+"1.Calculator With Try..Except"+"*"*5)


def calculator_with_try_except():
    """
    This function shows the use of try,except for input value validation.
    """

    def numbers_addition(number_one, number_two):
        """
        Addition of two integer numbers.
        Parameters:
            number_one:A decimal integer
            number_two:A decimal integer


        Returns:
            int:Addition of two integers
        """
        return number_one+number_two

    def numbers_subtraction(number_one, number_two):
        """
        Subtraction of two integer numbers.
        Parameters:
            number_one:A decimal integer
            number_two:A decimal integer


        Returns:
            int:Subtraction of two integers
        """
        return number_one-number_two

    def numbers_multiplication(number_one, number_two):
        """
        Multiplication of two integer numbers.
        Parameters:
            number_one(int):A decimal integer
            number_two(int):A decimal integer


        Returns:
            int:Multiplication of two integers
        """
        return number_one*number_two

    def numbers_division(number_one, number_two):
        """
        Divsion of two integer numbers.
        Parameters:
            number_one(int):A decimal integer
            number_two(int):A decimal integer


        Returns:
            int(int):Division of two integers
        """
        try:
            return number_one/number_two
        except ZeroDivisionError:
            print("You have given zero as denominator value,please avoid it")

    def take_input():
        """
        This function takes input from user.
        Parameters:
            No input parameters.           

        Returns:
            number_one(int):A decimal integer
            number_two(int):A decimal integer
        """
        # following code checks,is the input is valid datatype or not.
        while True:
            try:
                number_one = int(input("Enter value of first number "))
                number_two = int(input("Enter value of second number "))
            except ValueError:
                print("You have entered wrong value for integer data type input.")
            else:
                return number_one, number_two

    print("Enter \"add\" for addition")
    print("Enter \"sub\" for subtraction")
    print("Enter \"mul\" for multiplication")
    print("Enter \"div\" for division")
    print("*"*50)
    # getting operation name from user
    operation = input("Enter operation from above list ")
    print("*"*50)
    if operation.lower() == "add":
        number_one, number_two = take_input()
        addition_result = numbers_addition(number_one, number_two)
        print("Addition of numbers entered by you is: ", addition_result)
    elif operation.lower() == "sub":
        number_one, number_two = take_input()
        subtraction_result = numbers_subtraction(number_one, number_two)
        print("Subtraction of numbers entered by you is: ", subtraction_result)
    elif operation.lower() == "mul":
        number_one, number_two = take_input()
        multiplication_result = numbers_multiplication(number_one, number_two)
        print("Multiplication of numbers entered by you is: ",
              multiplication_result)
    elif operation.lower() == "div":
        number_one, number_two = take_input()
        division_result = numbers_division(number_one, number_two)
        print("Division of numbers entered by you is: ", division_result)
    else:
        print("The operation you entered does not exist.")
    return


calculator_with_try_except()
print()

print("*"*5+"2.Checking Input Value Entered By User"+"*"*5)


def input_value_check_function():
    def check_function(input_value):
        """
        This function checks, what type of values we got and returns that value.
        Parameters:
            input_value(int):A decimal integer value

        Returns:
            input_value(int):A decimal integer value
        """
        # checking input value,according to type
        try:
            chr(input_value)
        except TypeError:
            # print(chr(None)),this gives TypeError
            # inappropriate argument type
            pass
        except NameError:
            # print(chr(ten)),this gives NameError
            # name not found globally
            pass
        finally:
            return input_value

    # to store input argument and its value
    result_dict = {}

    def super_function(number_one, number_two, number_three, number_four):
        """
        This function takes, input arguments and calls check_function.
        Parameters:
            number_one(int):A decimal integer value
            number_two(int):A decimal integer value
            number_three(int):A decimal integer value
            number_four(int):A decimal integer value

        Returns:
            result_dict:It contains variable name as key and input value as value
        """
        result_dict["number_one"] = check_function(number_one)
        result_dict["number_two"] = check_function(number_two)
        result_dict["number_three"] = check_function(number_three)
        result_dict["number_four"] = check_function(number_four)
        return result_dict

    #validation_result = super_function(None, 5, None, "three")
    validation_result = super_function(None, 5, None, None)

    # print(type(validation_result))
    print("Input values function got are:")
    for key, value in validation_result.items():
        print(key, ":", value)
    # print(chr(ten))
    # print(chr(None))
    return


input_value_check_function()
print()

print("*"*5+"3.Checking Parentheses Matching"+"*"*5)


def parentheses_matching_function():
    def are_pair(opening_element, closing_element):
        """
        This function checks that opening element is matching with closing element or not.
        Parameters:
            opening_element(str):opening bracket of expression
            closing_element(str):closing bracket of expression
        Returns:
            bool:opening and closing elements matching or not
        """
        if opening_element == "[" and closing_element == "]":
            return True
        elif opening_element == "(" and closing_element == ")":
            return True
        elif opening_element == "{" and closing_element == "}":
            return True
        else:
            return False

    expression = "(7+8*(9+10)*{2+3}/[8*5]})"
    print(expression)
    print(expression.split(" "))
    list_expression_one = []
    for value in expression:
        list_expression_one.append(value)
    print(list_expression_one)

    check_list = []

    def check_parentheses(list_expression):
        """
        This function checks the expression is valid or not.
        Parameters:
            list_expression(str)
        Returns:
            bool:Expression is valid or not
        """
        for index in range(len(list_expression)):
            if list_expression[index] in "({[":
                #print("Here closing bracket is opening : ", list_expression[index])
                check_list.append(list_expression[index])
                #print("Check list is: ", check_list)
            elif list_expression[index] in "]})":
                #print("Here closing bracket is : ", list_expression[index])
                if len(check_list) == 0 or not(are_pair(check_list[len(check_list)-1], list_expression[index])):
                    #print("Here one", check_list)
                    return False
                else:
                    #print("Here two", check_list)
                    check_list.pop()
        if len(check_list) == 0:
            #print("I am in final call")
            return True
        else:
            return False

    check_result = check_parentheses(list_expression_one)
    if check_result == True:
        print("Expression is parentheses matched")
    else:
        print("Expression is not parentheses matched")
    return


parentheses_matching_function()
print()

print("*"*5+"4.Modified Password Generator"+"*"*5)


def super_modified_password_generator():
    """
    This function generates the password as per user requirements.
    """
    import string
    import random
    import os
    # password should contain characters in range 5 to 10
    # password should contain uppercase alphabets
    # password should contain digits
    # password should contain only "*","#","!","%","$", these special characters
    # the number alphabets,digits and special character required in password,will be entered by user
    # the characters in password should be unique,no repeatation allowed
    while(True):
        while(True):
            try:
                password_size = int(input("Enter size for the password "))
                while(password_size):
                    if password_size < 5 or password_size > 10:
                        print("Password size should be between 5 to 10.")
                        password_size = int(
                            input("Enter size for the password. "))
                    else:
                        break
            except ValueError:
                print("You entered wrong data value for numberic data,try again")
                break
            try:
                number_alphabets = int(
                    input("Enter how many alphabets you want in password: "))
                number_digits = int(
                    input("Enter how many digits you want in password: "))
                number_special_chars = int(
                    input("Enter how many special characters you want in password: "))
            except Exception:
                print("You entered wrong data value for numberic data,try again")
                break
            # random.sample gives unique elements from given sample set
            alphas = random.sample(string.ascii_uppercase, number_alphabets)
            digits = random.sample(string.digits, number_digits)
            special_chars = random.sample("*#!%$", number_special_chars)
            characters = alphas+digits+special_chars
            # random.shuffle ,shuffels the original list
            random.shuffle(characters)
            password = "".join(characters)
            if len(password) == password_size:
                print("Your password generated is: ", password)
                os._exit(0)
            else:
                print(
                    "You have done mistake in giving password length,please give right length of password")
    return


super_modified_password_generator()
print()
