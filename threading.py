#question_1
import time
import datetime
import threading

def wait(name, delay):
    for wait in range(5):
        print(name,datetime.datetime.now())
        time.sleep(delay)

threading.Thread(target=wait,args=("1st thread",4)).start()

print(80*"_")

#question_2
import time
import datetime
import threading

def count(name):
    for i in range(1,11):
        print(datetime.datetime.now())
        time.sleep(1)
        print(i)
threading.Thread(target= count,args=("thread",)).start()

print(80*"_")

#question_3
import time
import threading
pets = ['dog','cat','rat','nightangle','parrot']
def lis(x):
    for i in pets :
        x=2+x
        time.sleep(2+x)
        print('after %d sec delay :'%(x))
        print('%d list element is : '%pets.index(i),i)
a = 0
threading.Thread(target = lis, args = (a,)).start()

print(80*"_")

#question_4
import math
import time
import threading
a= int(input('enter number for finding factorial = '))
threading.Thread(target = math.factorial , args = (a,)).start()
factorial = math.factorial(a)
time.sleep(0.5)
print('0.5 sec. delay')
print('& The factorial of given number = ',factorial)





















