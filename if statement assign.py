
#question_1(1800,1900,2100,2200 and 2300 are not leap years but gets divisible by 4)
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")    
print(30*"#")

#question_2
length=float(input("Enter the length=\t"))
breadth=float(input("Enter the breadth=\t"))
if(length==0 or breadth==0):
    print('''Dimention has to be something!''')
if (length==breadth):
    print("It is a square.")
else:
    print("It is a rectangle.")
print(30*"#")

#question_3
age_1=int(input("Enter the age of first person=\t"))
age_2=int(input("Enter the age of second person=\t"))
age_3=int(input("Enter the age of third person=\t"))
if(age_1==age_2 and age_1>age_3 and age_2>age_3):
    print("both 1st person and 2nd person are oldest in the group")
elif(age_1==age_3 and  age_1>age_2 and age_3>age_2):
    print("both 1st person and 3rd person are oldest in the group")
elif(age_2==age_3 and age_2>age_1 and age_3>age_1):
    print("both 2nd person and 3rd person are oldest in the group")
elif(age_1==0 or age_2==0 or age_3==0):
    print("Are you a GOD or something!!!")
elif(age_1>age_2 or age_1>age_3):
    print("1st person is the oldest person.")
elif(age_2>age_1 or age_2>age_3):
    print("2nd person is the oldest person.")
elif(age_3>age_1 or age_3>age_2):
    print("3rd person is the oldest person.")
if(age_1==age_2 and age_1<age_3 and age_2<age_3):
    print("both 1st person and 2nd person are youngest in the group")
elif(age_1==age_3 and age_1<age_2 and age_3<age_2):
    print("both 1st person and 3rd person are youngest in the group")
elif(age_2==age_3 and age_2<age_1 and age_3<age_1):
    print("both 2nd person and 3rd person are youngest in the group")
elif(age_1<age_2 or age_1<age_3):
    print("1st person is the youngest person")
elif(age_2<age_1 or age_2<age_3):
    print("2nd person is the youngest person")
elif(age_3<age_1 or age_3<age_2):
    print("3rd person is the youngest person")
print(30*"#")

#question_4
points=float(input("enter your points=\t"))
if (points<=0 and points>200):
    print("Invalid input!!!")
if (points<=50):
    print("Sorry! No prize this time\t")
elif (points<=150):
    print("Congratulations! You won a wooden dog\t")
elif (points<=180):
    print("Congratulations! You won a book\t")
else:
    print("Congratulations! You won chocolates\t")
print(30*"#")

#question_5

print("For shoppers, shopping items more than worth of Rs:1000/-: May claim for 10% discount")
print("1 unit = Rs:100/-")
cost=100
unit=int(input("Number of units you have purchased=\t"))
bill=float(cost*unit)
if(unit<=0):
    print('''You haven't purchased anything''')
if(bill>1000):
    print("Your Original bill=\t",bill)
    bill=bill-(bill*0.1)
    print("your bill with 10% discount=\t",bill)
else:
    print("your bill=",bill)
print(30*"#")




    
    



        
