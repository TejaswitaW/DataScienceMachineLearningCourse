print("*"*5+"1.Functions as First Class Object"+"*"*5)


def functions_as_first_class_object():
    def square(number):
        return number*number

    # in python functions are first class objects.
    # here we assgined name of function to variable
    function = square
    print(square)
    # we can call function using other name
    ("Square of 16 is: ",print(function(16)))
    return


functions_as_first_class_object()
print()

def functions_as_first_class_object_one():
    def outerfun(number):
        def innerfun():
            #this is closure function
            print("I am inner function:", number)
        #returning function
        return innerfun  # returns object


    returned_function = outerfun(number=100)
    returned_function()
    del outerfun
    # we have deleted outerfun , but still returned_function will get executed
    returned_function()
    return
functions_as_first_class_object_one()
print()

def functions_as_first_class_object_three():
    def logger(msg):
        def log_message():
            #this is closure function
            print("Log: ", msg)
        # returning a function
        return log_message


    log_hi = logger("Hi!")
    #after returning from function, still return value remember argument
    log_hi()
    return
functions_as_first_class_object_three()
print()

def functions_as_first_class_object_four():
    import logging
    logging.basicConfig(filename="example.log", level=logging.INFO)
    # I want to keep log of name of function and arguments passed to a funciton
    # for keeping log, we have creatred example.log file

    def logger(func):
        def log_func(*args):
            #this is closure function
            logging.info("Running \"{}\" with argument {}".format(
                func.__name__, args))
            print("After {} call".format(func.__name__))
            print(func(*args))
        return log_func


    def add(x, y):
        return x+y


    def sub(x, y):
        return x-y


    add_logger = logger(add)
    sub_logger = logger(sub)

    add_logger(3, 3)
    add_logger(4, 5)

    sub_logger(10, 5)
    sub_logger(20, 10)
    return
functions_as_first_class_object_four()
print()

def creating_html_tag_using_closure():
    #use closure to create html tag
    def html_tag(tag):
        def wrap_text(msg):
            print("<{0}>{1}</{0}>".format(tag, msg))
        return wrap_text


    print_h1 = html_tag("h1")
    print_h1("Test Headline!")
    print_h1("Another Headline!")
    print_p = html_tag("p")
    print_p("Test Paragraph!")
    return
creating_html_tag_using_closure()
print()

print("*"*5+"2.Decorators in Python"+"*"*5)
def use_of_decorators():
    def decorator_function(original_function):
        def wrapper_function():
            print("I am adding new functionality to original function")
            original_function()
        return wrapper_function


    def display():
        print("I am original function")


    decorated_function = decorator_function(display)
    decorated_function()
    return
use_of_decorators()
print()

def use_of_decorators_one():
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print("I am adding new functionality to original function")
            original_function(*args, **kwargs)
        return wrapper_function


    @decorator_function
    def display():
        print("I am original display function")


    @decorator_function
    def display_info(name, age):
        print("I am original display_info function")
        print("Name of the person is: ", name)
        print("Age of the person is: ", age)


    display()
    display_info("Tom", 25)
    return
use_of_decorators_one()
print()

def use_of_decorators_two():
    a = int(input("Enter number one "))
    b = int(input("Enter number two "))


    def decorator(function):
        def wrapper(a, b):
            if b == 0:
                #checking if denominator is zero
                print("You can not divide by zero,Quit")
                return
            return function(a, b)
        return wrapper


    @decorator
    def divide(a, b):
        return a/b


    answer = divide(a, b)
    print("Result of division:",answer)
    return
use_of_decorators_two()
print()

def use_of_decorators_three():
    class DecoratorClass(object):
        #use init method to pass original function
        def __init__(self, original_function):
            self.original_function = original_function
        #__call__ method will behave like our wrapper function
        def __call__(self, *args, **kwargs):
            print("Call method executed,{}".format(
                self.original_function.__name__))
            return self.original_function(*args, **kwargs)


    @DecoratorClass
    def display():
        print("I am original function run")


    @DecoratorClass
    def display_info(name, age):
        print("Name of the person is: ", name)
        print("Age of the person is: ", age)


    display()
    display_info("Tom", 35)
    return
use_of_decorators_three()
print()