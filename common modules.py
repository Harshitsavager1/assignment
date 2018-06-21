#question_1
Time_tuple='''TIME TUPLE:We represent time in a way that’s easy for us to understand.
However, Python stores it in tuples.These python tuples are made of nine numbers.
Leap seconds are added to make up to Earth’s slowing rotation. When DST is 0,it isn’t
applied. When it’s 1, it is applied. However, when it is -1, it is up to the library
to determine that.This tuple has an equivalent struct_time structure. \n

(DST:DST is Daylight Saving Time, an adjustment of the timezone by (usually)one hour
during part of the year.)'''
print(Time_tuple)

print(82*"_")
#question_2
import datetime
current=datetime.datetime.now()
print(current.strftime("%d/ %B /%Y"))

print(82*"_")
#question_3
current = datetime.datetime.now()
print('The current date and time is = ',current.strftime("%d/ %m/ %Y"))
x=current.month
print("Extracted month is = ",x)

print(82*"_")
#question_4
current = datetime.datetime.now()
print("The current date and time is = ",current.strftime("%d/%m/%Y"))
x=current.day
print("Extracted day is = ",x)

print(82*"_")
#question_5
a = "2018-06-21"
date = datetime.datetime.strptime(a, "%Y-%m-%d")
print("The date is = ",date)
y=date.day
print("Extracted date from given time = ",y)

print(82*"_")
#question_6
import time
x = time.asctime(time.localtime())
print(x)

print(82*"_")
#question_7
import math
x=int(input("enter any number for which you want to find factorial = "))
print(math.factorial(x))
print(82*"_")
#question_8 (can be skipped acc. to sir)
#question_9
import os
print(os.getcwd())

print(82*"_")






