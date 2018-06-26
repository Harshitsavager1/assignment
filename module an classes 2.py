#question_1
class animal:
    def chara(self):
        print("- Contains prokaryotic cells")
        print("- They are multicellular")
        
class tiger(animal):
    def __init__(self):
        print('''**Tiger's characterstics**''')
x=tiger()
x.chara()

print(80*"!")

#question_2

print('''a.f() = A; b.f() = B''')
print('''a.g() = A; b.g() = B''')

print(80*"!")

#question_3

class cop():
    def __init__(self,name,age,work,experience,designation):
        self.name=name
        self.age=age
        self.work=work
        self.experience=experience
        self.designation=designation

    def display(self):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)

    def add(self):
        print("Add the following details",self.name)

    def update(self,n,a,w,e,d):
        self.name=n
        self.age=a
        self.work=w
        self.experience=e
        self.designation=d
        print("The updated info is:")
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)

    def updated(self):
        return(self.name,self.age,self.work,self.experience,self.designation)
x=cop('Employee name: Jojo','Age: 19','Work: Hire employee','Experience: 3yrs','Position: HR')
x.display()
x.update('Employee name: Sam','Age: 20','Work: Manages exployee work','Experience: 5yrs','Position: Manager')
class mission(cop):
    def add_mission(self):
        print("The mission is alloted to :",self.updated())
emp=mission('Employee Name = Sam','Age = 20','Work = Manages exployee work','Experience = 5yrs','Position = manager')
emp.add_mission()
        
print(80*"!")

#question_4
l = float(input("enter the len"))
b= float(input("enter the bre"))
a=float(input("enter the length of side of square"))
class shape:
    def __init__(self,l,b):
        
        self.length = l
        self.breadth = b

    def area(self,length,breadth):
        print("Area of given figure is = ", self.length*self.breadth)
        
class rec(shape):
    print("For area of rectangle: ")
x=rec(l,b)
x.area(l,b)

class sq(shape):
        print("For area of square: ")
y = sq(a,a)
y.area(a,a)

print(5*"Here it ends!!!")
