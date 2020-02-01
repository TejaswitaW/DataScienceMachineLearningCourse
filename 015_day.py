print("*"*5+" OOPs Concept "+"*"*5)
print()

print("@"*5+" Inheritance "+"@"*5)
print()

def use_inheritance_one():
    """
    This function tells how to use inheritance.
    """
    print("* use_inheritance_one() *")
    print()

    class Robot:
        def __init__(self, name):
            # this is constructor
            # initializes object
            self.name = name

        def say_hi(self):
            print("Hi, I am "+self.name)

    class PhysicianRobot(Robot):
        # this class inherit class Robot
        def say_hi(self):
            # if this method is not defined then base class method will get called
            print("Hi, I am not "+self.name)

    robo_one = Robot("Marvin")
    robo_two = PhysicianRobot("James")
    # returns class name with object address
    print(robo_one)
    print(robo_two)
    # returns class name
    print(type(robo_one))
    print(type(robo_two))
    robo_two.say_hi()
    return


use_inheritance_one()
print()


def use_inheritance_two():
    """
    This function tells how to use inheritance,
    how base class method is called when inherited class doen't define that method.
    """
    print("* use_inheritance_two() *")
    print()

    class Robot:
        def __init__(self, name):
            self.name = name

        def say_hi(self):
            print("Hi, I am "+self.name)

    class PhysicianRobot(Robot):
        # this class inherit class Robot
        # here say_hi method is not defined
        pass

    robo_one = Robot("Marvin")
    robo_two = PhysicianRobot("James")
    # returns class name with object address
    print(robo_one)
    print(robo_two)
    # returns class name
    print(type(robo_one))
    print(type(robo_two))
    robo_two.say_hi()
    print("Observe the output, of previous and this function")
    return


use_inheritance_two()
print()


def use_inheritance_three():
    """
    This function tells how to use inheritance, 
    and using base class name we can access base class method in inherited class.
    """
    print("* use_inheritance_three() *")
    print()

    class Robot:
        def __init__(self, name):
            self.name = name

        def say_hi(self):
            print("Hi, I am "+self.name)

    class PhysicianRobot(Robot):
        def say_hi(self):
            # if this method is not defined then base class method will get called
            # used base class name to access base class method
            Robot.say_hi(self)
            print("Everything will be okay!")
            print(self.name+" takes care of you")

    robo_one = Robot("Marvin")
    robo_two = PhysicianRobot("James")

    robo_two.say_hi()
    return


use_inheritance_three()
print()


def use_inheritance_four():
    """
    This function tells how to use inheritance,
    and how to use super() function to access base class method in inherited class.
    """
    print("* use_inheritance_four() *")
    print()

    class Robot:
        def __init__(self, name):
            self.name = name

        def say_hi(self):
            print("Hi, I am "+self.name)

    class PhysicianRobot(Robot):
        def say_hi(self):
            # if this method is not defined then base class method will get called
            # using super function to access base class method
            super().say_hi()
            print("Everything will be okay!,Now using super function")
            print(self.name+" takes care of you")

    robo_one = Robot("Marvin")
    robo_two = PhysicianRobot("James")

    robo_two.say_hi()
    return


use_inheritance_four()
print()


def use_inheritance_five():
    """
    This function tells how to use inheritance,
    and how to access class variable.
    """
    print("* use_inheritance_five() *")
    print()

    class Robot:
        _robot_count = 100

        def __init__(self, name):
            self._name = name
            Robot._robot_count += 1

        def say_hi(self):
            print("Hi, I am "+self._name)

    class PhysicianRobot(Robot):
        def say_hi(self):
            # if this method is not defined then base class method will get called.
            print("Hi, I am not "+self._name)
            print("Here accessing class variable: ", self._robot_count)

    robo_one = Robot("Marvin")
    robo_two = PhysicianRobot("James")

    print("Class variable access using class name: ", Robot._robot_count)
    print("Class variable access using inherited class: ",
          PhysicianRobot._robot_count)
    print("Class variable access using object of class: ", robo_one._robot_count)
    print("Class variable access using object of inherited class: ",
          robo_two._robot_count)
    print(robo_two._name)
    robo_two.say_hi()
    return


use_inheritance_five()
print()


def use_inheritance_six():
    """
    This function tells how to use inheritance,
    and private variable of class.
    """
    print("* use_inheritance_six() *")
    print()

    class Robot:
        _robot_count = 100

        def __init__(self, name):
            # private variable of class
            self.__name = name
            self._name = "John Smith"

        def say_hi(self):
            print("Hi, I am "+self.__name)
            print("Hi, I am "+self._name)

    class PhysicianRobot(Robot):
        def say_hi(self):
            super().say_hi()
            print("Hi, How are you")
            print("Please read following comments")
            # as it is private thus get error
            # print(self.__name)

    robo_one = Robot("Marvin")
    robo_two = PhysicianRobot("James")
    print(robo_one.say_hi())
    print("Please read these comments")
    # private variable of class we can not access using object name
    # following statement gives error
    # print(robo_one.__name)
    return


use_inheritance_six()
print()

print("@"*5+" MRO "+"@"*5)
print()


def mro_in_inheritance_one():
    """
    This function explains MRO(Method Resolution Order) in inheritance.
    """
    print("* mro_in_inheritance_one() *")
    print()

    class PersonName:
        def __init__(self):
            self.name = "John"
            self.age = 23

        def get_name(self):
            return self.name

    class ActorName:
        def __init__(self):
            self.name = "Richard"
            self.age = 32

        def get_name(self):
            return self.name

    class Name(PersonName, ActorName):
        def __init__(self):
            PersonName.__init__(self)
            ActorName.__init__(self)

        def get_name(self):
            return self.name

    human_name = Name()
    print(human_name.get_name())
    return


mro_in_inheritance_one()
print()


def mro_in_inheritance_two():
    """
    This function explains MRO(Method Resolution Order) in inheritance.
    """
    print("* mro_in_inheritance_two() *")
    print()

    class PersonName:
        def __init__(self):
            self.name = "John"
            self.age = 23

        def get_name(self):
            return self.name

    class ActorName:
        def __init__(self):
            self.name = "Richard"
            self.age = 32

        def get_name(self):
            return self.name

    class Name(PersonName, ActorName):
        def get_name(self):
            return self.name

    human_name = Name()
    print(human_name.get_name())
    return


mro_in_inheritance_two()
print()


def mro_in_inheritance_three():
    """
    This function explains MRO(Method Resolution Order) in inheritance.
    """
    print("* mro_in_inheritance_three() *")
    print()

    class PersonName:
        def __init__(self):
            self.name = "John"
            self.age = 23

        def get_name(self):
            return self.name

    class ActorName:
        def __init__(self):
            self.name = "Richard"
            self.age = 32

        def get_name(self):
            return self.name

    class Name(ActorName, PersonName):
        def get_name(self):
            return self.name

    human_name = Name()
    print(human_name.get_name())
    return


mro_in_inheritance_three()
print()


def mro_in_inheritance_four():
    """
    This function explains MRO(Method Resolution Order) in inheritance.
    """
    print("* mro_in_inheritance_four() *")
    print()

    class PersonName:
        def __init__(self):
            self.name = "John"
            self.age = 23

        def get_name(self):
            return self.name

    class ActorName:
        def __init__(self):
            self.name = "Richard"
            self.age = 32

        def get_name(self):
            return self.name

    class Name(ActorName, PersonName):
        def get_name(self):
            return self.name

    human_name = Name()
    print(human_name.get_name())
    print("The MRO for class \"Name\" is: ")
    print(Name.__mro__)
    return


mro_in_inheritance_four()
print()

print("@"*5+" Abstract Base Class "+"@"*5)
print()


def use_abstract_base_class_one():
    """
    This method explains abstract base class,we can not instantiate abstract base class.
    """
    print("* use_abstract_base_class_one() *")
    print()
    from abc import ABC, abstractmethod

    class Polygon(ABC):

        # abstract method
        @abstractmethod
        def no_of_sides(self):
            pass

    class Triangle(Polygon):

        # overriding abstract method
        def no_of_sides(self):
            print("I am Triangle,I have 3 sides")

    class Pentagon(Polygon):

        # overriding abstract method
        def no_of_sides(self):
            print("I am Pentagon,I have 5 sides")

    class Hexagon(Polygon):

        # overriding abstract method
        def no_of_sides(self):
            print("I am Hexagon,I have 6 sides")

    class Quadrilateral(Polygon):

        # overriding abstract method
        def no_of_sides(self):
            print("I am Quadrilateral,I have 4 sides")

    # Driver code
    shape_one = Triangle()
    shape_one.no_of_sides()

    shape_two = Quadrilateral()
    shape_two.no_of_sides()

    shape_three = Pentagon()
    shape_three.no_of_sides()

    shape_five = Hexagon()
    shape_five.no_of_sides()
    print("Please read following comments")
    # TypeError: Can't instantiate abstract class Polygon with abstract methods no_of_sides
    # shape_six = Polygon()
    # shape_six.no_of_sides()
    return


use_abstract_base_class_one()
print()


def use_abstract_base_class_two():
    """
    This function tells about, issubclass and isinstance built_in functions.
    """
    print("* use_abstract_base_class_two() *")
    print()
    from abc import ABC, abstractmethod

    class Parent(ABC):
        @abstractmethod
        def geeks(self):
            print("I am abstract method")

    class Child(Parent):
        def geeks(self):
            print("child class")

    # returns true,
    # if a class supplied as
    # the first argument is the subclass of another class supplied as the second argument
    # else it returns false
    print(issubclass(Child, Parent))
    # returns True if the object is instance of class
    print(isinstance(Child(), Parent))
    # p1 = Parent()#error
    return


use_abstract_base_class_two()
print()
