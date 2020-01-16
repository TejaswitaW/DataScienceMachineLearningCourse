print("*"*5+"1.Use of Decorator in Calculator Assignment"+"*"*5)


def use_decorator_in_calculator():
    """
    This function performs the task of mathematical operation, entered by user.
    """
    def decorator(original_function):
        """
        This function adds some additional functionality to original function.
        """
        def wrapper_function(number_1, number_2):
            """
            This function does the task of validation.
            """
            if number_1 > 0 and number_2 > 0:
                return original_function(number_1, number_2)
            else:
                print("You entered wrong values,Quit")
                return
        return wrapper_function

    @decorator
    def numbers_addition(number_one, number_two):
        """
        Addition of two integer numbers.
        """
        return number_one+number_two

    @decorator
    def numbers_subtraction(number_one, number_two):
        """
        Subtraction of two integer numbers.
        """
        return number_one-number_two

    @decorator
    def numbers_multiplication(number_one, number_two):
        """
        Multiplication of two integer numbers.
        """
        return number_one*number_two

    @decorator
    def numbers_division(number_one, number_two):
        """
        Divsion of two integer numbers.
        """
        return number_one/number_two

    print("Enter \"add\" for addition")
    print("Enter \"sub\" for subtraction")
    print("Enter \"mul\" for multiplication")
    print("Enter \"div\" for division")
    print("*"*50)
    # getting operation name from user
    operation = input("Enter operation from above list ")
    print("*"*50)
    if operation.lower() == "add":
        number_one = int(input("Enter value of first number "))
        number_two = int(input("Enter value of second number "))
        addition_result = numbers_addition(number_one, number_two)
        print("Addition of numbers entered by you is: ", addition_result)
    elif operation.lower() == "sub":
        number_one = int(input("Enter value of first number "))
        number_two = int(input("Enter value of second number "))
        subtraction_result = numbers_subtraction(number_one, number_two)
        print("Subtraction of numbers entered by you is: ", subtraction_result)
    elif operation.lower() == "mul":
        number_one = int(input("Enter value of first number "))
        number_two = int(input("Enter value of second number "))
        multiplication_result = numbers_multiplication(number_one, number_two)
        print("Multiplication of numbers entered by you is: ",
              multiplication_result)
    elif operation.lower() == "div":
        number_one = int(input("Enter value of first number "))
        number_two = int(input("Enter value of second number "))
        division_result = numbers_division(number_one, number_two)
        print("Division of numbers entered by you is: ", division_result)
    else:
        print("The operation you entered does not exist")
    return


use_decorator_in_calculator()
print()

print("*"*5+"2.Use of Dictionary of Functions in Calculator Assignment"+"*"*5)


def use_dictionary_of_function_in_calculator():
    def decorator(original_function):
        """
        This function adds some additional functionality to original function.
        """
        def wrapper_function(number_1, number_2):
            """
            This function does the task of validation.
            """
            if number_1 > 0 and number_2 > 0:
                return original_function(number_1, number_2)
            else:
                print("You entered wrong values,Quit")
                return
        return wrapper_function

    @decorator
    def numbers_addition(number_one, number_two):
        """
        Addition of two integer numbers.
        """
        return number_one+number_two

    @decorator
    def numbers_subtraction(number_one, number_two):
        """
        Subtraction of two integer numbers.
        """
        return number_one-number_two

    @decorator
    def numbers_multiplication(number_one, number_two):
        """
        Multiplication of two integer numbers.
        """
        return number_one*number_two

    @decorator
    def numbers_division(number_one, number_two):
        """
        Divsion of two integer numbers.
        """
        return number_one/number_two

    functions_dictionary = dict(a=numbers_addition, s=numbers_subtraction,
                                m=numbers_multiplication, d=numbers_division)
    print("Enter \"a\" for addition")
    print("Enter \"s\" for subtraction")
    print("Enter \"m\" for multiplication")
    print("Enter \"d\" for division")
    print("*"*50)
    # getting operation name from user
    operation = input("Enter operation from above list ")
    print("*"*50)
    if operation.lower() == "a":
        number_one = int(input("Enter value of first number "))
        number_two = int(input("Enter value of second number "))
        # using dictionary key,accesing function and passing arguments
        addition_result = functions_dictionary["a"](number_one, number_two)
        print("Addition of numbers entered by you is: ", addition_result)
    elif operation.lower() == "s":
        number_one = int(input("Enter value of first number "))
        number_two = int(input("Enter value of second number "))
        # using dictionary key,accesing function and passing arguments
        subtraction_result = functions_dictionary["s"](number_one, number_two)
        print("Subtraction of numbers entered by you is: ", subtraction_result)
    elif operation.lower() == "m":
        number_one = int(input("Enter value of first number "))
        number_two = int(input("Enter value of second number "))
        # using dictionary key,accesing function and passing arguments
        multiplication_result = functions_dictionary["m"](
            number_one, number_two)
        print("Multiplication of numbers entered by you is: ",
              multiplication_result)
    elif operation.lower() == "d":
        number_one = int(input("Enter value of first number "))
        number_two = int(input("Enter value of second number "))
        # using dictionary key,accesing function and passing arguments
        division_result = functions_dictionary["d"](number_one, number_two)
        print("Division of numbers entered by you is: ", division_result)
    else:
        print("The operation you entered does not exist")
    return


use_dictionary_of_function_in_calculator()
print()

print("*"*5+"3.Modified Random Password Generator"+"*"*5)


def modified_random_password_generator():
    """
    This function generates password of specified length, according to users requirment.
    """
    import string
    import random
    while(True):
        # take length of password from user
        password_size = int(input("Enter size for the password: "))
        # password length should be between 5 to 10
        while(password_size):
            if password_size < 5 or password_size > 10:
                print("Password size should be between 5 to 10")
                password_size = int(input("Enter size for the password: "))
            else:
                break
        # take number of alphabets user wants in password
        number_alphabets = int(
            input("Enter how many alphabets you want in password: "))
        # take number of digits user wants in password
        number_digits = int(
            input("Enter how many digits you want in password: "))
        # take number of special characters user wants in password amongst #,!,%,$
        number_special_chars = int(
            input("Enter how many special characters you want in password: "))
        # use random.sample to get specified number of unique elements in password
        # random.sample returns list
        alphas = random.sample(string.ascii_uppercase, number_alphabets)
        digits = random.sample(string.digits, number_digits)
        special_chars = random.sample("*#!%$", number_special_chars)
        characters = alphas+digits+special_chars
        # random.shuffle , it shuffles original list
        random.shuffle(characters)
        password = "".join(characters)
        # checking length of generated password and password_size entered by user
        # if lengths are different then again loop will get executed
        if len(password) == password_size:
            print("Your password generated is: ", password)
            break
        else:
            print(
                "You have done mistake in giving password length,please give right length of password"+".")
    print("Done!!!!")
    return


modified_random_password_generator()
print()
