#question_1
f = open("demofile.txt", "w")

f.write('''Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. 
Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” 
That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. 
“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. 
They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. 
That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird''')
print(f)

f.close()

print(f.closed)

print(80*"_")
#question_2
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))

print(80*"_")
#question_3
with open("demofile.txt")as a:
    with open("xyz.txt","w")as b:
        for line in a:
            b.write(line)
f.close()
print(f.closed)
print(80*"_")

#question_4
with open("xyz.txt")as c,open("demofile.txt")as d:
    for l1, l2 in zip(c,d):
        print(l1+l2)
f.close()
print(f.closed)
print(80*"_")

#question_5
import random
f=open('ran.txt','w')
for i in range(10):
    data=str(random.randint(1,10))
    f.write(data)
    f.write("\n")
f.close()
print("\ndone")
file1=open("ran.txt",'r')
file2=open("sort.txt",'w')
list1=file1.readlines()
list1.sort()
file2.writelines(list1)
file1.close()
file2.close()



print(80*"_")











        
