import os
print("Implementation of bubble sort algorithm")


def bubble_sort():
    # first for loop traverse whole list
    # in each pass small numbers will get bubbled up by one position,
    # and highest number will go to last position in the list.
    # second for loop will iterate over reduced list's length-1,as
    # we get highest number at the last of the list, that we dont need to swap.
    # in this way small numbers will get bubbles up and larger numbers will get,
    # downside postions in list
    # list's elements should be homogeneous
    numbers_list = [1, 2, 3, 100, 50, 60, 70,
                    90, 0, 10, 5, 8, 120, 90, 87, -2, -100, 23, 54]
    print("Our original list is: ", numbers_list)
    for index_one in range(len(numbers_list)):
        for index_two in range(len(numbers_list)-index_one-1):
            # using this loop highest number will go at last position in list
            if numbers_list[index_two] > numbers_list[index_two+1]:
                temp = numbers_list[index_two]
                numbers_list[index_two] = numbers_list[index_two+1]
                numbers_list[index_two+1] = temp
    # print(numbers_list)
    print("Our sorted list is: ", end="")
    for i in range(len(numbers_list)):
        print(numbers_list[i], end=" ")
    return


bubble_sort()
print()

print("Implementation of bubble sort algorithm,by using pythonic way for swapping")


def bubble_sort_one():
    numbers_list = [1, 2, 3, 100, 50, 60, 70,
                    90, 0, 10, 5, 8, 120, 90, 87, -2, -100, 23, 54]
    print("Our original list is: ", numbers_list)
    for index_one in range(len(numbers_list)):
        for index_two in range(len(numbers_list)-index_one-1):
            # using this loop highest number will go at last position in list
            if numbers_list[index_two] > numbers_list[index_two+1]:
                numbers_list[index_two], numbers_list[index_two +
                                                      1] = numbers_list[index_two+1], numbers_list[index_two]
            # print(numbers_list)
    print("Our sorted list is: ", end="")
    for i in range(len(numbers_list)):
        print(numbers_list[i], end=" ")
    return


bubble_sort_one()
print()


print("Implementation of function to get directories and files in path using os module's scandir() function")


def using_os_module_scanning_flies_dirs_in_path():
    def scandirs(path):
        for entry in os.scandir(path):
            # type of entry is <class 'nt.DirEntry'>
            if not entry.name.startswith(".") and entry.is_file():
                # I don't want to include files which start with "."
                # type of entry.name is str
                yield entry.name
            elif entry.is_dir() and not entry.name.startswith(".") and not entry.name.startswith("_"):
                # I don't want to scan dir like .vscode,_pychache_
                path_two = path + "\\"+entry.name
                print("-"*70)
                print("Path is %s" % path_two)
                print("-"*70)
                # scandirs returns generator
                file_generator = scandirs(path_two)
                for my_file in file_generator:
                    print(my_file)
    # write your file path here.
    path = "D:\\Radical Course"
    dir_entry_object = os.scandir(path)
    # type of dir_entry_object <class 'nt.ScandirIterator'>
    print("!"*70)
    print("Files and directories in %s" % path)
    print("!"*70)
    for entry in dir_entry_object:
        if entry.is_dir():
            path_one = path+"\\"+entry.name
            print("*"*70)
            print("Path is %s" % path_one)
            print("*"*70)
            file_generator = scandirs(path_one)
            for my_file in file_generator:
                print(my_file)
        elif entry.is_file:
            print(entry.name)
    # to close the iterator and
    # free acquired resources
    dir_entry_object.close()

    # scandir.close() method is called automatically
    # when the iterator is exhausted
    # or garbage collected, or
    # when an error happens during iterating.
    return


using_os_module_scanning_flies_dirs_in_path()
print()
