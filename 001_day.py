print("*"*5+"Basics of Data Structures in Python"+"*"*5)
print()
print("-----Basics of Tuple-----")


def studying_tuple():
    """
    This function explains about tuple.
    """
    tuple_one = ()
    tuple_two = tuple()
    print("Creating empty tuple: ", tuple_one)
    print("Creating empty tuple: ", tuple_two)
    tuple_two = tuple(range(10))
    print("Tuple created using range: ", tuple_two)
    tuple_one = (11, 22, 33, 44, 55, 66, 77)
    print("Created tuple is: ", tuple_one)
    print("Accessing element using element index,tuple_one[2]: ", tuple_one[2])
    # returns tuple
    sliced_elements = tuple_one[2:]
    print("Sliced elements from the tuple are: ", sliced_elements)
    tuple_two = (1, 2, 3, 4, "tom", 3.14, 7+4j, True)
    print("New tuple is: ", tuple_two)
    three_tuple = 3, 4.6, "dog"
    print("New tuple is: ", three_tuple)
    string_tuple = ("hello",)
    # <class 'tuple'>
    print("Type of tuple is: ", type(string_tuple))
    data_tuple = ("mouse", [8, 4, 6], (1, 2, 3), 110, 134, 167, "mouse")
    print("Original data tuple is: ", data_tuple)
    # using nested indexing accessing tuple element
    print("Element data_tuple[0][3] we got is: ", data_tuple[0][3])
    print("Element data_tuple[1][1] we got is: ", data_tuple[1][1])
    # negative indexing
    print("Accessing last element from tuple using negative index: ",
          data_tuple[-1])
    print("Use index method to get index of element,data_tuple.index(\"mouse\"): ",
          data_tuple.index("mouse"))
    print("Use count method to get number of count of element,data_tuple.count(\"mouse\"): ",
          data_tuple.count("mouse"))
    # join two tuples
    tuple_one = ("a", "b", "c")
    tuple_two = (1, 2, 3)
    tuple_three = tuple_one+tuple_two
    print("tuple_one is: ", tuple_one)
    print("tuple_two is: ", tuple_two)
    print("Joined tuple of above two tuple is: ", tuple_three)
    print("Length of tuple_three is,len(tuple_three): ", len(tuple_three))
    print("We can delete entire tuple using \" del data_tuple \"")
    return


studying_tuple()
print()
print("-----Basics of Dictionary-----")


def studying_dictionary():
    """
    This function explains about dictionary.
    """
    # creating empty dictionary
    dict_one = {}
    print("Our dictionary dict_one is: ", dict_one)
    dict_one = {"name": "Tom", "age": 25, "salary": 100000}
    print("Our dictionary dict_one is: ", dict_one)
    # access value using key
    print("Accessing value of key name as,dict_one[name]: ", dict_one["name"])
    # access all keys and values from dictionary
    print("All keys and values in dictionary: ")
    for key, value in dict_one.items():
        print("key is {} and value is {}".format(key, value))
    # access all keys of dictionary
    print("All keys in dict_one are: ")
    for key in dict_one.keys():
        print(key, end=" ")
    # access all values of dictionary
    print()
    print("All values in dict_one are: ")
    for value in dict_one.values():
        print(value, end=" ")
    # accesing value using get method
    print()
    dict_value = dict_one.get("name")
    print("Got value is: ", dict_value)
    # if key is not exist ,get method returns default value
    # if we access using key, if key does not exist, it gives key error
    dict_value = dict_one.get("city", "Bangalore")
    print("Got value is: ", dict_value)
    print("Observe the difference in above ouputs")
    key_list = [1, 2, 3, 4, 5, 6]
    data_dict = dict.fromkeys(key_list, 100)
    print("Our data_dict is: ", data_dict)
    print("clear() method removes all elements from dictionary")
    data_dict.clear()
    print("After clear operation data_dict is: ", data_dict)
    key_list = [1, 2, 3, 4, 5, 6]
    data_dict = dict.fromkeys(key_list, 100)
    print("Our dictionay is: ",data_dict)
    print("Copy retruns copy of dictionary")
    new_data_dict = data_dict.copy()
    print("Our copied dictionary is: ", new_data_dict)
    print("ID of data_dict is: ", id(data_dict))
    print("ID of new_data_dict is: ", id(new_data_dict))
    print("pop() method removes element with specified key: ", data_dict.pop(1))
    print("After pop() our dictionary becomes: ", data_dict)
    print("popitem() method removes last inserted key, value pair: ", data_dict.pop(6))
    print("After popitem() our dictionary becomes: ", data_dict)
    print("setdefault(),returns the value of the specified key,if the key does not exist insert the key,with the specified value")
    returned_value = data_dict.setdefault("car", "BMW")
    print("Returned value is: ", returned_value)
    print("Our dicitonary is: ", data_dict)
    print("Using update method , we can specified key and value pairs: ")
    print("Our dicitonary data_dict is: ", data_dict)
    print("Original dictionary dict_one is: ",dict_one)
    ky_values=(("company","jp morgan"),("fav_food","cookies"),("hobby","singing"))
    dict_one.update(ky_values)
    print("After updation our dictionary dict_one becomes: ",dict_one)
    print("Delete specifed key using key,del dict_one[\"fav_food\"]")
    del dict_one["fav_food"]
    print("After deletion of key, \"fav_food\" our dictionary becomes: ",dict_one)
    print("We can delete whole dictionary,\"del dict_one\"")
    del dict_one
    return


studying_dictionary()
print()
