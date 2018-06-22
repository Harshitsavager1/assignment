#question_1
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
         print("The area of circle = %d  "%(self.radius**2*3.14))
    
    def circumference(self):
        print("The circumference of circle = %f"%(2*self.radius*3.14))
r=float(input("Enter the radius of circle ="))
circ_1 = Circle(r)
circ_1.circumference()
circ_1.area()

print(80*"_")
#question_2
class Student():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def disp(self):
        print('''Student's name = %s'''%(self.name))
        print('''Student's roll no. = %d'''%(self.roll))
a = str(input("Enter your name = "))
b = int(input("Enter your roll no. = "))
stu = Student(a,b)
stu.disp()

print(80*"_")
#question_3
class Temperature():
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit
      
    def  convertFahrenhiet(self):
        f = (self.celsius*(9/5))+32
        print("%d celsius = %f fahrenheit"%(self.fahrenheit,f))
        
    def convertCelcius(self):
        c = (self.fahrenheit-32)*(5/9)
        print("%d fahrenheit = %f celsius"%(self.celsius,c))
celc = float(input("Enter temperature in celsius = "))
fa = float(input("Enter temperature in fahrenheit = "))
t = Temperature(celc,fa)
t.convertCelcius()
t.convertFahrenhiet()

print(80*"_")

#question_4
class movie_details():
    def __init__(self,a,b,c,d):
        self.movie=a
        self.artist=b
        self.year=c
        self.rating=d
    def display(self):
        return("Name of the movie is %s done by artist %s and released in year %d which has raiting of %d star"%(self.movie,self.artist,self.year,self.rating))
    def update(self,new):
        self.movie=new
x=input("Enter the name of movie")
y=input("Enter the name of artist")
z=int(input("Release date of movie"))
p=int(input("Enter the rating of movie"))
obj=movie_details(x,y,z,p)
print(obj.display())
q=input("enter new movie")
obj.update(q)
print(obj.display())

print(80*"_")

#question_5
class outlay:
    def __init__(self,out,saved):
        self.out=out
        self.saved=saved
    def disp_info(self):
        print("The monthly outlay of income is %d"%(self.out))
        print("The monthly savings from income is %d"%(self.saved))
    def calculate_s(self):
        self.sal = self.out + self.saved
    def display_s(self):
        print("Total salary is %d"%(self.sal))
info = int(input("Enter the outlay of income"))
save = int(input("Enter savings from income"))
M = outlay(info,save)
M.disp_info()
M.calculate_s()
M.display_s()

print(80*"_")




