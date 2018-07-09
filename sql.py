#question_1_2_3
'''
Q.1- Create a database. Create the following tables:
1. Book
2. Titles
3. Publishers
4. Zipcodes
5. AuthorsTitles
6. Authors
Q.2- Insert values in the tables.
Q.3- Update any values in any of the tables. Print the original and updated values.'''




import pymysql as pm

try:
    con = pm.connect(host='localhost', database='book', user='root',password='6428')
    print('''connection estalished''')
    cursor = con.cursor()

    query = 'create table book(Book_ID int(5) primary key,Title_ID int(10),Location varchar(13),genre char(10))'
    cursor.execute(query)

    
    
    query_insert = "insert into book values(%s,%s,%s,%s)"
    data = [(1216602,2,'3rd shelf','fiction'),
            (1216603,3,'4th shelf','comic'),
            (1216604,4,'5th shelf','sarcasm')]

    cursor.executemany(query_insert, data)
    query_show="select * from book"
    cursor.execute(query_show)
    data=cursor.fetchall()
    for row in data:
        print("book:{},title:{},publishers:{},zipcodes:{},authorstitles:{},authors{}")
    query_update="update book set Book_ID=1216616 where Title_ID=9"

    cursor.execute(query_update)
    query_show="select * from book"
    cursor.execute(query_show)
    data1=cursor.fetchall()
    for row in data1:
        print("book:{},title:{},publisher:{},zipcodes:{},authorstitles:{},authors:{}")
    con.commit()
    print("table created")
    
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print(e)
finally:
    con.close()
    cursor.close()











   
