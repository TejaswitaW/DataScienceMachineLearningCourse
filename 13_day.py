print("*"*5+"OOPs Concepts"+"*"*5)


def use_of_class():
    """
    This function tells about basics of classes.
    """
    class Calculator:
        """
        This class does arithmetic operations on data.
        """

        def __init__(self, number_one, number_two):
            """
            This is constructor function of class.
            """
            # number_one and number_two are instance variables of class
            self.number_one = number_one
            self.number_two = number_two

        def add(self):
            """
            This function does addition of two integer numbers.
            """
            # this is instance method of class
            return self.number_one+self.number_two

    # creating object of class
    calci_object = Calculator(10, 15)
    # using object calling method
    result = calci_object.add()
    print("Addition of two numbers is: ", result)
    return


use_of_class()
print()


def use_of_class_variable():
    """
    This function tells about the use of class variable.
    """
    class Person:
        """
        This is person class.
        """
        # this is class variable
        # it is common for all objects
        population = 0

        def __init__(self, name, age):
            self.name = name
            self.age = age
            Person.population += 1

        def how_many(self):
            print(Person.population)

        def __str__(self):
            return self.name+" "+str(self.age)

    person_one = Person("Tom", 35)
    print("Till now population is: ")
    person_one.how_many()
    print(person_one)
    new_object = Person("Justin", 25)
    print("Till now population is: ")
    new_object.how_many()
    print(new_object)
    return


use_of_class_variable()
print()


def getting_class_attribute():
    """
    This function tells how to access class attributes.
    """
    class Person:
        """
        This is person class.
        """
        population = 0

        def __init__(self, name, age):
            self.name = name
            self.age = age
            Person.population += 1

        def how_many(self):
            print(Person.population)

        def __str__(self):
            return self.name+" "+str(self.age)

    person_one = Person("Tom", 35)
    print(person_one)
    # accessing class attributes
    print("Attribute \"__name__\"", Person.__name__)
    print("Attribute \"__doc__ \"", Person.__doc__)
    print("Attribute \"__module__\"", Person.__module__)
    print("Attribute \"__dict__\"", Person.__dict__)
    return


getting_class_attribute()
print()


def use_of_utility_funtions():
    """
    This function tells how to use utility function.
    """
    class Person:
        """
        This is person class.
        """
        population = 0

        def __init__(self, name, age):
            self.name = name
            self.age = age
            Person.population += 1

        def how_many(self):
            print(Person.population)

        def __str__(self):
            return self.name+" "+str(self.age)

    person_one = Person("Tom", 15)
    print("Use of setattr()")
    # we can create new attribute
    print(setattr(person_one, "name", "Tejawita"))
    print(person_one)
    print("Use of hasattr()")
    # check if the object has given name attribute
    # returns boolean value
    print(hasattr(person_one, "name"))
    print("Use of delattr()")
    # deletes the named attribute of an object
    # does not return any value i.e None
    print(delattr(person_one, "name"))
    print(hasattr(person_one, "name"))
    setattr(person_one, "name", "Elon")
    print("Use of getattr()")
    # method returns the value of the named attribute of an object
    # if not found, it returns the default value provided to the function
    print(getattr(person_one, "name"))
    new_object = Person("Justin", 25)
    print(getattr(new_object, "name"))
    return


use_of_utility_funtions()
print()


def calculator_program_using_class():
    """
    This function shows use of classes and instance methods to create calucator.
    """
    import os

    class Calculator:
        """
        The model builds calculator for doing arithmetic operations.
        """

        def __init__(self, number_one, number_two):
            self.number_one = number_one
            self.number_two = number_two

        def add(self):
            """
            This function returns addition of two integers.
            """
            return self.number_one+self.number_two

        def sub(self):
            """
            This function returns subtraction of two integers.
            """
            return self.number_one-self.number_two

        def mul(self):
            """
            This function returns multiplication of two integers.
            """
            return self.number_one*self.number_two

        def div(self):
            """
            This function returns division of two integers.
            """
            if self.number_two == 0:
                print("You can not divide any number by 0")
                return None
            return self.number_one/self.number_two

    cal_one = Calculator(90, 0)
    print("Addition: ", cal_one.add())
    print("Subtraction: ", cal_one.sub())
    print("Multiplication: ", cal_one.mul())
    print("Division: ", cal_one.div())
    return


calculator_program_using_class()
print()


def private_methods_in_class():
    class Method:
        """
        We have created private method in class.
        """
        # private function

        def __private_method(self):
            print("I am private method")

        def using_private_method(self):
            self.__private_method()

    method_object = Method()
    print("Please read comments")
    # the private method of class we can not call it outside of the class
    # method_object.__private_method()
    # AttributeError: 'Method' object has no attribute '__private_method'
    print("Accessing private method using instance method of class")
    method_object.using_private_method()
    return


private_methods_in_class()
print()
