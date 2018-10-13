import calendar
import time
# cal = calendar.calendar(2018)
# print(cal)

# q = calendar.isleap(2000)
# # print(q)

# print(calendar.leapdays(1999,2001))

# print(calendar.month(2018,10))

# print(calendar.monthrange(2018,10))

# print(calendar.weekday(2018,10,10))

# print(time.timezone)

# print(time.daylight)

# print(time.time())

# print(time.localtime().tm_year)

# print(time.asctime())

# print(time.ctime())
# print(type(time.ctime()))

# print(time.clock())

# for i in range(10):
#     print(i)
#     time.sleep(1)

# def p():
#     time.sleep(2)
# t0 = time.clock()
# p()
# t1 = time.clock()
# t2 = int(t0)
# t3 = int (t2)
# print(t1 - t0)

# print(help(time.strftime))


# import locale
# from time import strftime,localtime
# # print(strftime("%Y-%m-%d %H:%M:%S",localtime()))
# t = time.localtime()
# ft = time.strftime("%Y-%m-%d %H:%M",time.localtime())
# print(ft)
# print(strftime("%Y{y}%m{m}%d{d} %H:%M:%S").format(y="年",m="月",d="日"))

from datetime import datetime
# dt = datetime(2018,10,11)
# # print(dt.today())
# # print(dt.now())
# # print(dt.fromtimestamp(time.time()))

# from datetime import datetime,timedelta
# t1 = datetime.now()
# print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# td = timedelta(days = 1)
# print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))

# def p():
#     time.sleep(5)
# t1 = time.time()
# p()
# t2 = time.time()
# print(t2-t1)

import timeit
# c = """
# sum = []
# for i in range(1000):
#     sum.append(i)
# """
# sum = []
# def p():
#     for i in range(1000):
#         sum.append(i)
#
# t1 = timeit.timeit(stmt= c ,number=100000)
# print("t1=",t1)
# t2 = timeit.timeit(stmt="[i for i in range(1000)]",number = 100000)
# print("t2=",t2)
# t3 = timeit.timeit(stmt=p,number=100000)
# print("t3=",t3)


# s="""
# sum = []
# def p(m):
#     for i in range(m):
#         sum.append(i)
#         print(sum)
# """
# t = timeit.timeit("p(m)",setup=s+"m=3",number=10000000)

import os
# myd = os.getcwd()
# print(myd)

# os.chdir()

# ld = os.listdir()
# print(ld)
#
# rst = os.makedirs("exp")
# print(rst)

# rst = os.system("touch lulu.doc")
# print(rst)

# print(os.name,os.linesep)

import os.path as op
# absp = op.abspath(".")
# print(absp)
# bn = op.basename("/pythonidea")
# print(bn)

# e = op.exists("p01")
# d = op.exists("p01.py")
# print(e,d)

# rst = os.system("touch lulu.txt")
# print(rst)


import shutil
# rst = shutil.copy("p01.py","p11.py")
# print(rst)

# rst = shutil.copyfile("notebook.md","p02.py")
# print(rst)

# rst = shutil.move("exp/p11.py","p11.py")
# print(rst)

import zipfile,os
# zf = zipfile.ZipFile("p11.zip",mode="a")
# print(zf.getinfo("p11.py"))
# nl = zf.namelist()
# rst = zf.extractall("exp")
# print(nl)

import random
# rst = [str(i)+"lulu" for i in range(10)]
# l = random.choice(rst)
# print(l)

# l1 = [i for i in range(10)]
# print(l1)
# random.shuffle(l1)
# print(l1)
l1 = []
for i in range(1011):
    rst =  random.randint(0,100)
    l1.append(rst)
print(min(l1),max(l1))

