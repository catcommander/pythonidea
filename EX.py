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

class Student():
    name = "lulu"
    agr = 18
    def say(self):
        self.name = "goddess"
        self.age = 16
        print("she is {0}".format(self.name))
        print("she age is {0}".format(self.name))
lulu = Student()
lulu.say()









