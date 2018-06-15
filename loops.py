#question_1
x=10
while(x>0):
   y=int(input("enter any integer"))
   x=x-1
   print("the no. is ",y)
print(30*"@")
#question_2
n =int(input("Enter number"))
a=1
while a<6:
    print(a)
    a += 2

#question_3
list_1=[]
for i in range(0,5):
   number = int(input("enter a number:"))
   list_1.append(number)
print("list is :',list_1")
list_2 = []
for i in list_1:
      num = i*i
      list_2.append(num)
print("new list is= ",list_2)
print(30*"@")
#question_4
list_1=[8,2,"xyz",2.8,"abc",7.2]
int_list=[]
str_list=[]
float_list=[]
print("the list is",list_1)
for i in list_1:
      if(type(i)==int):
          int_list.append(i)
      elif(type(i)==str):
          str_list.append(i)
      elif(type(i)==float):
          float_list.append(i)
print("the integer list is=",int_list)
print("the string list is=",str_list)
print("the float list is=",float_list)
print(30*"@")

#question_5
list_1=[]
list_2=[]
for i in range(1,101):
      if(i%2==0):
          list_1.append(i)
      else:
          list_2.append(i)
print("the even list is= ",list_1)
print("the odd list is= ",list_2)
print(30*"@")

#question_6
for i in range(0,5):
      print('*'*i)
print(30*"@")

#question_7

dict={"one":1,"two":2,"three":3}
for i in range(len(dioct)):
       print("The elements =",dict[i])

print(30*"@")      

    

