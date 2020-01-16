print("*"*5+"Basic Intuitions In Python"+"*"*5)

print("*"*5+"1.Basic Intuitions Related to function"+"*"*5)


def functions_as_first_class_object():
    """
    This function shows the functions are first class objects.
    """
    print("**"+"Understand functions in python are first class objects"+"**")

    def addition_function(number_one, number_two):
        return number_one+number_two

    addition_result = addition_function(1, 2)
    # getting type of addtion_function
    print("Type of addition_function is: ", type(addition_function))
    print("ID of addition_function is: ", id(addition_function))
    addition_function_object = addition_function
    del addition_function
    # as we have deleted addition_function, still we can access it using its another reference.
    addition_result = addition_function_object(5, 6)
    print("ID of addition_function_object is: ", id(addition_function_object))
    print("Observe that both IDs are same")
    print("Result of addition is: ", addition_result)
    return


functions_as_first_class_object()
print()

print("*"*5+"2.Basic Intuitions Related to Lists"+"*"*5)


def observe_list_related_intuition_one():
    """
    This function shows lists related intuition.
    """
    print("**"+"Understand list object in python"+"**")
    list_one = [1, 2, 3]
    list_two = [1, 2, 3]
    print("Our list one is: ", list_one)
    print("Our list two is: ", list_two)
    print("ID of list one is: ", id(list_one))
    print("ID of list two is: ", id(list_two))
    print("As references of two different lists with same values are different so we got for (list_one is list_two) : ", list_one is list_two)
    print(id(list_one), id(list_one[0]), id(list_one[1]))
    print(id(list_two), id(list_two[0]), id(list_two[1]))
    print("Observe above that,list_one and list_two has different IDs,\nbut their individual elements have same ID ")
    return


observe_list_related_intuition_one()
print()


def observe_list_related_intuition_two():
    """
    This function shows lists related intuition.
    """
    print("**Observe the list object ID, when we pass list as an argument to a function**")

    def use_list_function(test_list):
        print("Inside the function ID of argument passed test_list is: ", id(test_list))
        # following code will do changes in our original list
        test_list[0] = 10
        print("After adding element at 0th position list becomes: ", test_list)
        test_list = [1, 2, 3, 4, 5]
        print("ID of newly created test_list list inside function", id(test_list))
        print("Our newly created list inside function is: ", test_list)
        print("Observe that ,if we create new list with same list with same name then new list object will get created.")

    test_list = [8, 9, 10]
    print("Our original list is: ", test_list)
    print("ID of test_list outside the function use_list_function:", id(test_list))
    use_list_function(test_list)
    print("Our test_list after use_list_function call:", test_list)
    print(test_list)
    return


observe_list_related_intuition_two()
print()

print("*"*5+"3.dir() Function "+"*"*5)


def use_of_dir_function():
    """
    This function tells how to use dir() function.
    """
    print("**Understand that,\nthe dir() function returns all properties and methods of the specified object,\nwithout the values.**\n")
    number = 100
    print("*"+"-"*10+"Observe Properties and Methods of integer object"+"-"*10+"*\n")
    print(dir(number))
    print()
    print("*"+"-"*10+"Used built in method __add__(10) on int object number=100,so result is" +
          "-"*10+":", number.__add__(10))
    print()

    class Person:
        name = "John"
        age = 36
        country = "Norway"
    print("*"+"-"*10+"Observe we used dir on user defined class Person"+"-"*10+"*\n")
    print(dir(Person))
    print()
    string = "Tom"
    print("*"+"-"*10+"Observe Properties and Methods of string object"+"-"*10+"*\n")
    print(dir(string))
    return


use_of_dir_function()
print()

print("*"*5+"4.__doc__attribute "+"*"*5)


def use_of_doc_attribute():
    """
    This function shows use of __doc__ attribute.
    """
    print("**Understand that,\nthe __doc__ attribute provide a convenient way of associating documentation,\nwith python modules,functions,classes and methods**\n")
    number = 100
    print("*"+"-"*10+"Observe documentation of integer object"+"-"*10+"*")
    print(number.__doc__)

    class Person:
        """
        This is individual person class.
        """
        name = "John"
        age = 36
        country = "Norway"
    print("*"+"-"*10+"Observe we used __doc__ on user defined class Person"+"-"*10+"*")
    print(Person.__doc__)
    string = "Tom"
    print("*"+"-"*10+"Observe documentation of string object"+"-"*10+"*")
    print(string.__doc__)
    return


use_of_doc_attribute()
print()

print("*"*5+"5.Observe IDs of Objects "+"*"*5)


def observe_ids_of_objects():
    """
    This function tells about same references of object. 
    """
    number_one = 10
    number_two = 10
    print("ID of number_one when,number_one=10 is ", id(number_one))
    print("ID of number_two when,number_two=10 is ", id(number_two))
    print("Observe the IDs are same, as both variables have same value less than 256 ")
    # number_one = 25890
    # number_two = 25890
    # print("ID of number_one when,number_one=25890 is ",id(number_one))
    # print("ID of number_two when,number_two=25890 is ",id(number_two))
    # print("Observe the IDs are different, as both variables have different value greater than 256 ")
    # print("For commented code ideally IDs should be different but,sometimes come same")
    number_one = 10+2
    print("ID of number_one = 10+2: ", id(number_one))
    number_one = 12  # a=13
    print("ID of number_one = 12: ", id(number_one))
    number_one = 13  # a=13
    print("ID of number_one = 13 : ", id(number_one))
    print("Observe IDs of above objects")
    return


observe_ids_of_objects()
print()
