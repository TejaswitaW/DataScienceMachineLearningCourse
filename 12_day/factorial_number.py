#facto_number = 1


def facto(number):
    if number == 1:
        return number
    else:
        return number*facto(number-1)
#    return facto_number


number = int(input("Enter the number, to find factorial : "))
facto_number = facto(number)
print("Factorial of number is : ", facto_number)
