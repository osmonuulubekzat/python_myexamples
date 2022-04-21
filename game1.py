# bir sandyn kaysi sandarga bolunushunu tabuu
# def find(number):
#     array = []
#     for i in range(1, number+1):
#         if number % i == 0:
#             array.append(i)
#     return array
# while True:
#     enter = input("enter value: ")
#     if enter == "exit":
#         break
#     else:
#         enter = enter.strip()
#         print(find(int(enter)))

# Maximum of two numbers in Python
#  the first selustion
def maxsimum(a, b):
    if a >= b:
        return a
    else:
        return b


# print(max(15,89))
a = 5
b = 10
maxoftwo = max(a, b)


# print(maxoftwo)

# print(a if a >= b else b)
# -------------------------------------
# Python program maximum of three
# def muxsimum(a,b,c):
#     if a >= b and a >= c:
#         largest = a
#     elif b >= a and b >=c:
#         largest = b
#     elif c >= a and c >= b:
#         largest = c
#     return largest
#
#
# print(muxsimum(12, 15, 60))
# def add(a, b, c):
#     list = [a, b, c]
#     return max(list)
# print(add(15,96,80))

# Driven code
# a = 10
# b = 14
# c = 12
# print(max(a, b, c))
# -------------------------
# Python program to find second largest number in a list
# 1)
# array = [20, 30, 40, 60, 70]
# lagest = max(array)
#
# def second(a):
#     for i in range(len(a)):
#         if a[i] == lagest:
#             a.pop(i)
#     return a
#
# print(max(second(array)))
# 2)
# array = [20, 30, 40, 60, 70]
# array.sort()
# print(array)
# print(array[-2])
# -----------
# 3)
# array = [20, 30, 40, 60, 70]
# new_array = array
# new_array.remove(max(new_array))
# print(max(new_array))
# --------------------------------------------------
# Python | Largest, Smallest, Second Largest, Second Smallest in a List

# array = [20, 30, 40, 60, 70, 80, 95, 84, 9, 6, 4, 2, 6, 8, 96]
# array.sort()
# print(array[-1])
# print(array[-2])
# print(array[0])
# print(array[1])

# ----------------------------------
## Python program to find smallest
# number in a list

# array = []
#
# enter = int(input('enter number of list'))
#
# for i in range(1, enter+1):
#     al = int(input("enter sumber: "))
#     array.append(al)
#
# print(min(array))

# Python program to print even numbers in a list

# array = [20, 30, 40, 60, 70, 80, 95, 84, 9, 6, 4, 2, 6, 8, 96]
#
# even_number = list(filter(lambda i: i % 2 == 0, array))
# print(even_number)
# ------------------
# odd number

# array = [20, 30, 40, 60, 70, 80, 95, 84, 9, 6, 4, 2, 6, 8, 96, 17, 3, 23]
# odd_number = list(filter(lambda i: i % 2 != 0, array))
# odd_number = list(filter(lambda i: i % 2 == 1, array))
# print(odd_number)
# ---------------------------
# Python program to count Even and Odd numbers in a List
# array = [20, 30, 40, 60, 70, 80, 95, 84, 9, 6, 4, 2, 6, 8, 96, 17, 3, 23]
# count_even = 0
# count_odd = 0
# for i in range(len(array)):
#     if array[i] % 2 == 0:
#         count_even += 1
#     else:
#         count_odd+=1
# print(count_even)
# print(count_odd)
# -------------------------------------------
# Program to print duplicates from a list of integers

# Получаем гласные
# def get_vowels(String):
#     return [each for each in String if each in 'aeiou']
# print(get_vowels("bekzat"))
# Первая буква в верхнем регистре
# def capitalize(String):
#     return String.title()
# print(capitalize("title"))
# Печать строки N раз
# n = 5
# string = 'hello'
# print(string * n)
# Объединяем два словаря
# def merge(dic1,dic2):
#     dic3 = dic1.copy()
# dic1.update(dic2)
# return dic1
# dic1={1:"hello", 2:"world"}
# dic2={3:"Python", 4:"Programming"}
#
# print(merge(dic1, dic2))
# Проверка дубликатов
# def check_duplicate(lst):
#     return len(lst) != len(set(lst))
# liste = [5,7,8,9,6,4,3,2]
# print(check_duplicate(liste))
# Фильтрация значений False
# def Filtering(lst):
#     return list(filter(None, lst))
# liste = [None,1,6,8,""]
# print(Filtering(liste))
# def ByteSize(stirng):
#     return len(stirng.encode("utf8"))
# print(ByteSize("hello"))
# Перемешивание списка
# from random import shuffle
# my_list1=[1,2,3,4,5,6]
# my_list2=["A","B","C","D"]
# shuffle(my_list1) # [4, 6, 1, 3, 2, 5]
# demo = shuffle(my_list2) # ['A', 'D', 'B', 'C']
# print(demo)
# def find(lst):
#     return max(lst)
# lst = {1,54,5,2}
# print(find(lst))
# class Armor:
#
#     def __init__(self, armor: float, description: str, level: int = 1):
#         self.armor = armor
#         self.level = level
#         self.description = description
#
#     def power(self) -> float:
#         return self.armor * self.level
#
# armor = Armor(5.2, "Common armor.", 2)
# armor.power()
# 10.4
#
# print(armor)
# <__main__.Armor object at 0x7fc4800e2cf8>
# from datetime import date
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def formBothYear(cls, name, year):
#         return cls(name, date.today().year - year)
#     @staticmethod
#     def isAbsult(age):
#         return age > 18
#
# person = Person("Asiya", 2)
# man = Person.formBothYear("Asiya", 2020)
# print(person.age)
# print(man.age)
# print(person.isAbsult(2))
# Remove all duplicates from a given string in Python
# def removeDuplicate(str):
#     s = set(str)
# The join in Python takes all the elements of an iterable and joins them into a single string.
# s = "-".join(s)
# s = "::".join(s)
# print(s)

# str="geeksforgeeks"
# removeDuplicate(str)
# get current time in python
# from datetime import datetime
# now = datetime.now().strftime("%H:%M:%S")
# print(now)

# def add(number:int,name:str):
#     print("integer is {} string is {}".format(number, name))
#
# add("5","Asiya")
# def i (a):
#     return int(a)
# print(i("5"))
# class Find:
#     def __init__(self, start: int, end: int, array=[]):
#         self.start = start
#         self.end = end
#         self.array = array
#
#     def set(self):
#         for i in range(self.start, self.end+1):
#             if i % 2 != 0:
#                 self.array.append(i)
#         return sum(self.array)
# emty = []
# c = Find(10, 20)
#
# print(c.set())
# from  datetime import datetime
#
# class Message():
#     def __init__(self, message, sender, time):
#         self.message = message
#         self.sender = sender
#         self.time = time
#         self.isRead = False
#     def show_message(self):
#         print("message:{}\nsender:{} \ntime:{}\nisRead:{}".format(self.message, self.sender, self.time, self.isRead))
#
#     def make_message_true(self):
#         self.isRead = True
#
#     def send_message(self, text):
#         pass
#
#     def newMessages(self, array_message: list):
#         array = []
#         for i in array_message:
#             if i.isRead == False:
#                 array.append(i.message)
#         return array
# message1 =  Message("hello  I am a message 1", "Asiya", datetime.now().strftime("%H:%M:%S"))
# message2 =  Message("hello  I am a message 2", "Asiya", datetime.now().strftime("%H:%M:%S"))
# message3 =  Message("hello  I am a message 3", "Asiya", datetime.now().strftime("%H:%M:%S"))
# message1.make_message_true()
# message2.make_message_true()
# # message1.show_message()
# ms = [message1, message2, message3]
# print(message1.newMessages(ms))
# class Quiz:
#     def __init__(self, question, chose: list, true_answer):
#         self.question = question
#         self.chose = chose
#         self.true_answer = true_answer
#     def show(self):
#         print("question: {}".format(self.question))
#         char = ["A", "B", "C", "D"]
#         for i in range(len(self.chose)):
#             print("{}){}".format(char[i], self.chose[i]))
#
# q1 = Quiz("the best programming langugae?",['pyhton','go','java','c++'],'python')
# q2 = Quiz("capital of Kyrgyzstan?", ['Tokio', 'Masscow', 'Bishkek', 'Tashkent'], 'Bishkek')
# q3 = Quiz("what is your daughter name?", ['Kamila', 'Asiya', 'Kadicha', 'Asel'], 'Asiya')
# functions = [q1, q2, q3]
# counter = 0
#
# while True:
#         functions[counter].show()
#         counter += 1
#         break

# def loop():
#     def getValue():
#         counter = int(input("san: ").strip())
#         return counter
#     conunt = getValue()
#     c = 0
#     if conunt != 0:
#         amount = 0
#         for i in range(conunt):
#             print(conunt)
#             amount += conunt
#             conunt -= 1
#             c+=1
#         total = amount / c
#         print(total)
#         loop()
#     else:
#         print('end of the loop')
# loop()
