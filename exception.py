#question_1
"ZeroDivisionError: division by zero"
def mail_me():
    print("send mail")
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)

except ZeroDivisionError as b:
    print("A Zero division error")
    mail_me()
    print(b)
print(80*"_")

#question_2 (IndexError: list index out of range)
l=[1,2,3]
try:
    print(l[3])
except Exception as e:
    print("error due to index error")
    print(e)
print(80*"_")

#question_3
print("NameError: Hi there")
print(80*"_")

#question_4
print("-5.0")
print("a/b result in 0")

print(80*"_")

#question 5
try:
    from hash import *
except Exception as e :
    print('Import error  :')
    print(e)    
fruits = ['Apple','Mango','Orange']
try :
    fruits[3]
except Exception as e :
    print('''the index error  :''')
    print(e)
x = 'tomato'
try :
    int(x)
    
except Exception as e :
    print('''The value error :''')
    print(e)
print(80*"_")
#question 6
class teens(Exception):
    def __init__(self,age):
        self.age = age
        print('''Rules for Voting: Candinate's age should be above 18 years, and your age is %d'''%(self.age))
def p_age():
    try :
        a = int(input('''enter your age :'''))
        if a<18 :
            raise teens(a
                        )
        print('''so now you can vote, buddy''')
        print('''Yea, thats exactly how it feels to be an adult one :p''')
    except teens as err :
        print('''you are under age,can't give vote''')
        p_age()
p_age()
print(80*"_")

































