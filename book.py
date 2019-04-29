import mysql.connector


def insert(cursor):
    query = 'INSERT INTO book(isbn,title,price) VALUES (%s,%s,%s)'
    cursor.execute(query, ('0385514239','Origin',2995))


def update(cursor):
    query = 'UPDATE book SET price=%s WHERE isbn=%s'
    cursor.execute(query, (29.95,'0385514239'))


try:
    cnx = mysql.connector.connect(host='localhost', user='root', password='vwxyz', database='demo')
    cursor = cnx.cursor()

    insert(cursor)
    cnx.commit()

    update(cursor)
    cnx.commit()

    cursor.close()
except mysql.connector.Error as err:
    print(err)
finally:
    try:
        cnx
    except NameError:
        pass
    else:
        cnx.close()