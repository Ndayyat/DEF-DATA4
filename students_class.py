# class Student:

#     def __init__(self,name, age, classs, test1, test2, test3):
#         self.name = name
#         self.age = age
#         self.classs = classs
#         self.test1= test1
#         self.test2 = test2
#         self. test3 = test3
        
#     def average(self):

#         return (self.test1 + self.test2 + self.test3) / 3


# John = Student("John", "20", "year6", 20, 40, 20 )
# finalmark= John.average()
# print(John.name, finalmark)


# class budget:

#     def __init__(self, food, clothing, entertaiment)
#          self.food = food
#          self.clothing = clothing
#          self.entertaiment = entertaiment

#     moneyin = ()
#     moneyout = ()
#     balance      

# from abc import ABC, abstractmethod

# import pdb

# pdb.set_trace()


# class Bird(ABC):
#     fly = True
#     babies = 0

#     def noise(self):
#         return "Squawk"

#     def reproduce(self):
#         self.babies += 1

#     @abstractmethod
#     def eat(self):
#         pass

#     extinct = False

# class Owl(Bird):

#     def reproduce(self):
#         self.babies += 6

#     def eat(self):
#         return "Peck peck"    


file = open("teams.txt", "a")
newline = ("this is a new line")
file.write(newline)

file.close()
# chars = file.read()


# print(chars[0], end="")
# print(chars[4],"")


# # for i in range(5):
# #     chars = file.readline()
# # # file.seek(0)
# # # file.write
# #     print(chars[0]+ chars[2])
# file.close()
