#定义一个空的类
class Student():
    #此处pass代表直接跳过，pass必须有
    pass
#定义一个对象
lulu = Student()

class PythonStudent():
    name = "luluu璐"
    age = 18
    course = "Python"

    def doHomework(self):
        print("I,在做作业！")
        #推荐在函数末尾使用return语句
        return None
#实例化一个叫lulu的学生，是一个具体的人
lulu = PythonStudent()
print(lulu.name)
print(lulu.age)
#注意成员函数的调用没有传递进入参数
lulu.doHomework()

