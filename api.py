#question_1
a=('''*XML
-User can argue endlessly about the "right" way to use XML. 
-XML is a markup language (A markup language is a way of adding extra information to
 free-flowing plain)
- XML's sweet spot is document markup.
-XML example <Person> is a record and <Relatives> is a list, but they are not
 identified as such by the syntax.''')
print(a)

b=('''*json
-JSON is a way of representing objects (as also noted in its name).
-An object notation like JSON is not as flexible.
-it has less redundant repetition of names.
- it has a defined way of distinguishing between a "record"and a "list".''')
print(b)

print(80*"_")

#question_2
import socket

def get_ips_for_host(host):
    try:
        ips = socket.gethostbyname_ex(host)
        ipc = socket.gethostbyname_ex(host)
        
    except socket.gaierror:
        ips=[]
        ipc=[]
    return ips , ipc
       

ips = get_ips_for_host('www.google.com')
ipc = get_ips_for_host('www.facebook.com')
print(repr(ips))
print(repr(ipc))

print(80*"_")

#question_3
c=('''The GET Method
GET is used to request data from a specified resource.''')

d=('''The POST Method
POST is used to send data to a server to create/update a resource.''')

e=('''The PUT Method
PUT is used to send data to a server to create/update a resource.''')

f=('''The DELETE Method
The DELETE method deletes the specified resource.''')

print(c)
print(d)
print(e)
print(f)

print(80*"_")

#question_4
g=('''API:
-API is an interface between two
software programs which facilitates
the interaction between them.
-API can be written in any language.
-API is the part of library''')

h=('''LIBRARY:
-A library contains many modules which are separated by its use.
-Library is written in same language which is a
collection of all the functionalities required for
the use case.

For example : Numpy is a library of Python, adding support for large, multi-dimensional
arrays and matrices, along with a large collection of high-level mathematical functions
to operate on these arrays.''')

print(g)
print(h)

print(80*"_")























































