print("*"*5+"1.File Handling"+"*"*5)


def open_file_function():
    """
    This function shows how to open file.
    """
    # if file does not exist in write mode, it will create file
    # default file open mode is read
    # file_handler is a file object using
    # this we can do operations on file
    file_handler = open("open_file_function.txt", "w")
    # following statement write data to our file
    file_handler.write("My name is Tom Hanks")
    # we should close file after use
    file_handler.close()
    return


open_file_function()
print()


def file_object_attributes():
    """
    This function tells about file object attributes.
    """
    file_handler = open("file_object_attributes.txt", "w")
    file_handler.write("My name is Tom Hanks")
    file_handler.close()
    # using file attributes we can access file properties
    print("File closed or not: ", file_handler.closed)
    print("File name: ", file_handler.name)
    print("File opened in access mode: ", file_handler.mode)
    print("File encoding: ", file_handler.encoding)
    return


file_object_attributes()
print()
print("*"*5+"2.File Handling Some Intuition"+"*"*5)


def file_handling_intuition_one():
    """
    This function tells about the "w" file access mode.
    """
    print("--Firt Function--")
    print("Opening same file twice in write mode, does not give error")
    file_handler = open("file_intu_one.txt", "w")
    file_handler.write("How are you?")
    file_handler = open("file_intu_one.txt", "w")
    # new content for file overwrite old content
    file_handler.write("I am fine")
    file_handler.close()
    return


file_handling_intuition_one()
print()


def file_handling_intuition_two():
    """
    This function tells about the "r" file access mode.
    """
    print("--Second Function--")
    # we are reading previous function file
    print("Opening same file twice in read mode, does not give error")
    file_handler = open("file_intu_one.txt", "r")
    print(file_handler.read())
    print("Return type of file read function is: ", type(file_handler.read()))
    print("Following does not read anything from file,as file is at the EOF")
    print(file_handler.read())
    file_handler.close()
    return


file_handling_intuition_two()
print()


def file_handling_intuition_three():
    """
    This function tells how to read specified number of characters from file.
    """
    print("--Third Function--")
    print("Reading some content from the file")
    file_handler = open("file_intu_one.txt", "r")
    # we need to give number of characters as argument to read function
    print(file_handler.read(5))
    file_handler.close()
    return


file_handling_intuition_three()
print()


def file_handling_intuition_four():
    """
    This function explains how "r+" file access mode works.
    """
    print("--Fourth Function--")
    file_handler = open("file_intu_one.txt", "r+")
    print(file_handler.read())
    # this mode append the new content in the file
    file_handler.write("abc")
    file_handler.close()
    file_handler = open("file_intu_one.txt", "r")
    print(file_handler.read())
    file_handler.close()
    return


file_handling_intuition_four()
print()


def file_handling_intuition_five():
    """
    This function explains how "w+" file access mode works.
    """
    print("--Fifth Function--")
    file_handler = open("file_intu_one.txt", "w+")
    # this mode is first write and then read
    # but I did reverse, so observe the output
    # and following statement does not read anything from file
    print(file_handler.read())
    # following line erased previous content from the file
    file_handler.write("abc")
    file_handler.close()
    print("Again calling read function, observe the output")
    file_handler = open("file_intu_one.txt", "r")
    print(file_handler.read())
    file_handler.close()
    return


file_handling_intuition_five()
print()


def file_handling_intuition_six():
    """
    This function explains how "w+" file access mode works.
    """
    print("--Sixth Function--")
    file_handler = open("file_intu_six.txt", "w+")
    # this mode is first write and then read
    file_handler.write("My new content to the file")
    # important to add following line
    # else you can not read from file
    file_handler.seek(0)
    print(file_handler.read())
    file_handler.close()
    return


file_handling_intuition_six()
print()


print("*"*5+"3.Use of With"+"*"*5)


def open_file_using_with():
    """
    This function shows how to open file using with statement.
    """
    with open("open_file_with.txt", "w") as file_handler:
        file_handler.write("My name is Tom Hanks, what is yours")
        # no need of close, it automatically closes the file
    return


open_file_using_with()
print()
