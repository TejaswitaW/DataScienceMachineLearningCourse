print("*"*5+" Basics of Data Structure in Python "+"*"*5)
print()

print("@"*5+" Basics of Lists "+"@"*5)
print()


def studying_lists():
    """
    This function explains the various functions and operations applied on list.
    """
    print("-----Creating List-----")
    print()
    # creating list
    list_one = [1, 2, 3, 4, 5, 6, 7]
    print("list_one is: ", list_one)
    print("Address of list_one is: ", id(list_one))
    # another way to create list
    list_two = list(range(10))
    print("list_two is: ", list_two)
    # creating blank list
    list_three = []
    print("list_three is: ", list_three)
    # getting length of list
    print("Length of list_one is: ", len(list_one))
    print()
    print("-----Operations on List-----")
    print()
    print("Accessing elements from list")
    print()
    data_list = [1, 2, [3, 4], 5, ["welcome", "to", "class"], 9, 10]
    print("Original list is: ", data_list)
    # accesing speciftied element from list
    # accessing "c" of string "class"
    print(data_list[-3][-1][-5])
    number_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print("number_list is: ", number_list)
    # slicing to get group of elements from list
    print("Accesing elements from index 2 to 5: ", number_list[2:6])
    print("Reversing number_list: ", number_list[::-1])
    print("Using negative index to access elements: ", number_list[-1:-6])
    print("Using negative index to access elements example: ",
          number_list[-6:-1])
    print("Slicing with step of 2: ", number_list[0:7:2])
    print("Slicing with step of 3: ", number_list[0:8:3])
    # creating new list using slicing
    new_one = number_list[0:4]
    print("new_one list is: ", new_one)
    new_two = number_list[4:]
    print("new_two list is: ", new_two)
    print()
    print("List modification methods")
    print()
    print("extend() method use")
    print()
    # syntax:list_name.extend(iterator)
    # extend method extends list with new iterator elements
    print("Original list is: ", number_list)
    number_list.extend([10])
    print("After appliying extend function on number_list: ", number_list)
    number_list.extend([10, 11, 12, 13])
    print("After appliying extend function on number_list, one: ", number_list)
    number_list.extend("tom")
    print("After appliying extend function on number_list, two: ", number_list)
    print()
    print("append() method use")
    print()
    # syntax:list_name.append(element)
    # append method insert element at the end of list
    print("Original list is: ", number_list)
    number_list.append([14, 15, 16])
    print("Use of append method: ", number_list)
    number_list.append("tim")
    print("Appended string in number_list: ", number_list)
    print()
    print("insert() method use")
    print()
    #syntax:list_name.insert(index, element)
    # insert method inserts element at specified index
    print("Our original list is: ", number_list)
    number_list.insert(0, 100)
    print("After inserting element at 0th position: ", number_list)
    number_list.insert(1, "hanks")
    print("After inserting element at 1st position: ", number_list)
    print()
    print("pop() method use")
    print()
    # syntax:list_name.pop()
    # syntax:list_name.pop(index)
    # removes and returns last element from the list
    print("Our original list is: ", number_list)
    print("We got last element: ", number_list.pop())
    print("After pop operation our list becomes: ", number_list)
    print("We got 3rd element from the list: ", number_list.pop(3))
    print("After pop operation our list becomes: ", number_list)
    print()
    print("clear() method use")
    print()
    # syntax: list_name.clear()
    # delete all elements from list
    # removes and returns last element from the list
    print("Our original list is: ", number_list)
    number_list.clear()
    print("After applying clear method on list: ", number_list)
    print()
    print("index() method use")
    print()
    number_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Our original list is: ", number_list)
    # syntax:list_name.index(2)
    # returns index of element
    print("Index of element 2 is: ", number_list.index(2))
    print()
    print("count()method use")
    print()
    # syntax:list_name.count(element)
    # returns number of occurences of element in the list
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 4, 4, 4, 4, 4, 4]
    print("Our list is: ", number_list)
    print("Number 4 occures:{} times ".format(number_list.count(4)))
    print()
    print("sort()method use")
    print()
    # syntax:list_name.sort()
    # returns the list in ascending order
    # list data should be homogeneous
    print("Our list is: ", number_list)
    number_list.sort()
    print("List after sort is: ", number_list)
    name_list = ["apple", "orange", "banana", "tamrind"]
    print("Our strings list is: ", name_list)
    name_list.sort()
    print("After sorting the name_list we got: ", name_list)
    print()
    print("reverse()method use")
    print()
    #syntax: list_name.reverse()
    # it reverses the original list
    print("Our original name_ list is: ", name_list)
    name_list.reverse()
    print("After applying reverse function on name_list: ", name_list)
    print()
    print("copy() method use")
    print()
    # syntax: list_two=list_one.copy()
    # creates new list object with different memory
    list_one = list(range(0, 5))
    list_two = list(range(11, 15))
    list_two = list_one.copy()
    print("list_two is: ", list_two)
    print("Observe addresses are different")
    print("ID of list_one is: ", id(list_one))
    print("ID of list_two is: ", id(list_two))
    list_three = list_one
    print("list_three is: ", list_three)
    print("Observe addresses are same")
    print("ID of list_three is: ", id(list_three))
    print("ID of list_one is: ", id(list_one))
    return


studying_lists()
print()

print("@"*5+" Basics of Sets "+"@"*5)
print()


def studying_sets():
    set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    print("Original set is: ", set_one)
    print()
    print("add()method use")
    print()
    # syntax:set_name.add(element)
    # method adds a given element to a set if the element is not present in the set
    print("Original set is: ", set_one)
    set_one.add(10)
    print("After adding 10 in set: ", set_one)
    print()
    print("update()method use")
    print()
    # syntax:set_name.update(iterable)
    # method updates the set, adding items from other iterable
    print("Original set is: ", set_one)
    set_one.update([11, 12, 13])
    print("After set update: ", set_one)
    print()
    print("discard() method use")
    print()
    # syntax:set_name.discard(element)
    # removes the element from the set only if the element is present in the set,
    # if the element is not present in the set,
    # then no error or exception is raised and the original set is printed
    print("Original set is: ", set_one)
    set_one.discard(11)
    print("After discard method use on set: ", set_one)
    print()
    print("remove() method use")
    print()
    # syntax:set_name.remove(element)
    # removes the specified element from the set,
    # method will raise an error if the specified item does not exist
    print("Original set is: ", set_one)
    set_one.remove(7)
    print("After remove method use on set: ", set_one)
    print()
    print("pop() method use")
    print()
    # syntax:set_name.pop()
    # removes a random element from the set and returns the removed element
    print("Original set is: ", set_one)
    print("After pop operation from set: ", set_one.pop())
    print()
    print("clear() method use")
    print()
    # syntax:set_name.clear
    # removes all elements from the set
    set_one.clear()
    print("After clear operation on set: ", set_one)
    print()
    print("Set Operations")
    set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set_two = {11, 2, 3, 14, 15, 16, 17, 8, 9}
    print("set_one is: ", set_one)
    print("set_two is: ", set_two)
    print()
    print("union() method")
    print()
    # syntax:setA | setB
    # syntax:setA.union(setB)
    # returns a set that contains all items from the original set, and all items from the specified sets.
    print("Union of set_one and set_two is: ", set_one | set_two)
    print("Union of set_one and set_two is: ", set_one.union(set_two))
    print()
    print("intersection() method")
    print()
    # syntax:setA & setB
    # syntax:setA.intersection(setB)
    # returns the largest set which contains all the elements that are common to both the sets
    print("Intersection of set_one and set_two is: ", set_one & set_two)
    print("Intersection of set_one and set_two is: ",
          set_one.intersection(set_two))
    print()
    print("difference() method")
    print()
    # syntax:setA - setB
    # syntax:setA.difference(setB)
    # returns the different elements between the number of elements in two sets
    print("Difference of set_one and set_two is: ", set_one-set_two)
    print("Difference of set_two and set_one is: ", set_two-set_one)
    print("Difference of set_one and set_two is: ", set_one.difference(set_two))
    print("Difference of set_two and set_one is: ", set_two.difference(set_one))
    print()
    print("symmetric_difference() method")
    print()
    # syntax:setA ^ setB
    # syntax:setA.symmetric_difference(setB)
    # returns the set of elements which are in either of the sets but not in both of them
    print("Symmetric Difference of set_one and set_two is: ", set_one ^ set_two)
    print("Symmetric Difference of set_one and set_two is: ",
          set_one.symmetric_difference(set_two))
    return


studying_sets()
print()
