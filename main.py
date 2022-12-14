import os
import keyword
from abc import ABC, abstractmethod
import threading
import multiprocessing

"""
print("OS module in python provides functions for interacting with OS.")
cwd = os.getcwd()
print("Current working directory - ", cwd)
# TO change directory - os.chdir('../')
# Creating a directory
print("1. os.mkdir()")
print("os.mkdir() method in Python is used to create a directory named path with the specified numeric mode.")
print("This method raises FileExistsError if the directory to be created already exists.")
print("2. os.makedirs()")
print("os.makedirs() method in Python is used to create a directory recursively.")
print("That means while making leaf directory if any intermediate-level directory is missing,")
print("os.makedirs() method will create them all.")
print("3. os.listdir()")
print("It is used to get list of all files and directories in the specified directory.")
print("If specific directory is not given, then the list of files and directories in the cwd will be returned.")
path = "./"
print(os.listdir(path))
print("4. os.remove()")
print("It removes or deletes a file path. This method cannot remove a directory.")
print("If the specified path is a directory then OSError will be raised by the method.")
# file = "file1.txt"
# location = ""
# path = os.path.join(location, file)
# os.remove(path)
print("By remove - file is deleted")
print("5. os.rmdir()")
print("os.rmdir() method in Python is used to remove or delete an empty directory.")
print("OS Error will be raised if the specified path is not an empty directory.")
# directory = "Del"
# location = ""
# path = os.path.join(location, directory)
# os.rmdir(path)
print("After a file or directory is deleted , the next time if a program is run - not found error is shown.")
# Commonly used functions
print("OS name - ", os.name)
list = keyword.kwlist
print(len(list))
print(list)
print("6. os.rename()")
print("Syntax- os.rename(filename, 'new_file.txt')")
print("7. os.remove()")
print("To remove a file we need to pass the name of the file as a parameter.")
# os.remove('file_name.txt')
print("8. os.path.exists('file_name)")
print("9. os.path.getsize('file_name')")

# Functional Programming
print("------Functional Programming--------------")
print("Its main focus is on ???what to solve??? in contrast to an imperative style where the main focus is ???how to solve???.")
print("It uses expressions instead of statements.")
print("An expression is evaluated to produce a value whereas a statement is executed to assign variables.")
print("Concepts -")
print("1. Pure Functions")

def pure_fx(List):
    List1= []
    for i in List:
        List1.append(i**2)
    return List1


l1 = [0, 2, 4, 6, 8, 10]
l2 = pure_fx(l1)
print("List 1", l1)
print("List 2", l2)
print("2. Recursion")
print("Recursion is a process in which a function calls itself directly or indirectly.")
def fact(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        return (n*fact(n-1))
num = 10
print("Factorial of", num, "is", fact(num))
print("3. Functions are First-Class")
print("Properties - ")
print("A function is an instance of the Object type.")
print("You can store the function in a variable.")
print("You can pass the function as a parameter to another function.")
print("You can return the function from a function.")
print("You can store them in data structures such as hash tables, lists.")
print("4. Immutability")
print("Immutability is a functional programming paradigm can be used for debugging")
print("as it will throw an error where the variable is being changed not where the value is changed.")
a = "Dhairya"
# a[1] = 'DS'  # TypeError
# Higher order functions
def val(func):
    dt = func("DhAiRyA")
    print(dt)
def up(text):
    return text.upper()
def lw(text):
    return text.lower()
val(up)
val(lw)

# Meta-Programming is the code that manipulates code.
# Metaclasses
a = 1
b = [1, 2, 3]
c = (1, 2, 3)
d = "SD"
print(type(a))
print(type(b))
print(type(c))
print(type(d))


class Student:
    pass


stu_obj = Student()

# Print type of object of Student class
print("Type of stu_obj is:", type(stu_obj))
print(type(Student))

# Enumerate - Enumerate Function adds counter to an iterable and also returns it.
l1 = ['D', 12, "S", False, 15]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(l1):
    print(index, item)

l2 = [i for i in l2 if i % 2 == 0]
print(l2)


# Abstract Classes
# A class which contains one or more abstract methods is called an abstract class.
# An abstract method is a method that has a declaration but does not have an implementation.
# Module name - ABC
# ABC works by decorating methods of the base class as abstract and then registering concrete classes as
# implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.


class Shape(ABC):
    @abstractmethod
    def parea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def parea(self):
        return self.length * self.breadth


class Square(Shape):
    type = "Square"
    sides = 4

    def __init__(self):
        self.length = 6

    def parea(self):
        return self.length * self.length


rect1 = Rectangle()
print(rect1.parea())

sq1 = Square()
print(sq1.parea())

# In the above example , abstract method is defined(no statements) and is called by rectangle and square class.

"""

# ----------------------Multithreading----------------------------
# Steps-
# 1. To import the threading module - import threading
# 2. To create a new thread, we create an object of Thread class. It takes following arguments:
#      target: the function to be executed by thread
#      args: the arguments to be passed to the target function
# 3. To start a thread, we use start method of Thread class.
# 4. Once the threads start, the current program (you can think of it like a main thread) also keeps on executing.
#    In order to stop execution of current program until a thread is complete, we use join method.


def printcube(num):
    print("Cube -", num * num * num)


def printsquare(num):
    print("Square -", num * num)


t1 = threading.Thread(target=printcube, args=(10,))
t2 = threading.Thread(target=printsquare, args=(10,))

t1.start()
t2.start()
t1.join()
t2.join()
print("Done")
"""
# -----------------------------------------------------------
def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
"""

