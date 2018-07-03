#question_1
import re
li = []
def email(email):
    username = re.split('[@.]',email)
    li.append(username)
email('zuck26@facebook.com')
email('page33@google.com')
email('jeff42@amazon.com')
print(li)
print(80*"_")


#question_2
import re
text = '''Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To 
make the bitter butter better.'''
m = re.findall(r'[bB]\w+', text)
print (m)

print(80*"_")


#question_3
import re
a = "A, very very; irregular_sentence"
r = re.findall(r"\w+",a)
print(r)
print(80*"_")

