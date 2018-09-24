# class Student():
#     name = "lulu"
#     age = 18
# Student.__dict__
# #实例化
# goddess = Student()
# goddess.__dict__
# print(goddess.name,goddess.age)

# class A():
#     name = "lulu"
#     age = 18
#     def a(self):
#         pass
# #此时A称为实例
# print(A.name,id(A.name))
# print(A.age,id(A.age))
# print("-"*20)
# a = A()
# print(A.__dict__)
# print(a.__dict__)
# print(a.name,id(a.name))
# print(a.age,id(a.age))
# print("-"*20)
# a.name = "luluu"
# a.age = 16
# print(a.__dict__)
# print(a.name,id(a.name))
# print(a.age,id(a.age))

# class Student():
#     name = "lulu"
#     age = 18
#     def say(self):
#         self.name = "goddess"
#         self.age = 16
#         print("she is {0}".format(self.name))
#         print("she age is {0}".format(self.age))
#     def sayagain():
#         print(__class__.name)
#         print(__class__.age)
# lulu = Student()
# lulu.say()
# Student.sayagain()

#关于self的案例
# class A():
#     name = "lulu"
#     age = 18
#     def __init__(self):
#         self.name = "snake"
#         self.age = 20
#     def say(self):
#         print(self.name)
#         print(self.age)
# class B():
#     name = "giao"
#     age = 30
#
# a = A()
# #此时，系统会默认把a作为第一个参数传入函数
# a.say()
# #此时self被a替换
# A.say(A)
# A.say(B)

# #在python中，任何类都有一个共同的父类叫object
# class Person():
#     #name是共有成员
#     name = "lulu"
#     #__age是私有成员
#     __age = 18
# p = Person()
# print(p.name)
# print(Person.__dict__)
# print(p._Person__age)


#在python中，任何类都有一个共同的父类叫object
# class person():
#     name = "lulu"
#     __age = 18
#     _petname = "sec"
#     def seelp(self):
#         print("sleeping....")
# class teacher(person):
#     def make_test(self):
#         person.seelp(self)
#         super().seelp()
# t = teacher()
# # print(t.name)
# # print(t._petname)
# t.make_test()

#构造函数
# class Dog():
#     #__init__就是构造函数
#     #每次实例化的时候，第一个被自动调用
#     def __init__(self):
#         print("I am init a dog")
# kaka = Dog()


# class Animal():
#     print("animal")
# class Reptile(Animal):
#     def __init__(self,name):
#         print("Reptile")
# class Crocodile(Reptile):
#     def __init__(self):
#         print("I am Crocodile" )
# class snake(Crocodile):
#     def __init__(self):
#         print("I am snake")
# c = snake()

# class A():
#     pass
# class B(A):
#     def __init__(self,name):
#         print("B")
#         print(name)
# class C(B):
#     def __init__(self):
#         B.__init__(self,"lulu")
#         print("C")
# s = C()
#

class Person():
    def sleep(self):
        print("sleep")
    def drink(self):
        print("drink")
    def __init__(self):
        print("eat")
class Teacher(Person):
    def word(self):
        print("work")
class Student(Person):
     def study(self):
         print("study")
class goddess(Teacher,Student):
    print("lulu喜欢")
lulu = goddess()
print(lulu)
print(issubclass(goddess,Teacher))
print(isinstance(lulu,goddess))
print(hasattr(Person,"sleep"))


