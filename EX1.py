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

t = time.localtime( )
ft = time.strftime("%Y年%m月%d %H:%M",t)
print(ft)





