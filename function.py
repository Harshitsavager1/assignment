#question_1
def area_of_circle(r):
    import math
    area = math.pi*r**2
    return area
r = float(input("Enter the Radius ="))
a = area_of_circle(r)
print("Area of circle= ",round(a,3))
print(30*"@")
#question_2
def divisiors(x):
    return [y for y in range(1, int(x / 2) + 1) if x % y == 0]
def perfect_numbers_in_range(a,b):
    return [x for x in range(a,b+1) if sum(divisiors(x)) == x]
print("So here are all perfect numbers which comes between 1-100= ",perfect_numbers_in_range(1, 100))
print(30*"@")
#question_3
def times_tables(n, t=1):
    if t == 13:
        return
    print(str(n) + "x" + str(t) + " = " + str(n*t))
    times_tables(n, t+1)
times_tables(int(input("Enter the number for which you want the times table = ")))
print(30*"@")
#question_4
def power(base,exponent):
    if(exponent==1):
        return(base)
    if(exponent!=1):
        return(base*power(base,exponent-1))
base=int(input("Enter base = "))
exponent=int(input("Enter the exponential value = "))
print("your answer = ",power(base,exponent))
print(30*"@")
#question_5
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter the number, you want the factorial for = "))
print("Factorial of given number = ")
print(factorial(n))         
print(30*"@")










