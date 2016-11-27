import sqlite3
con = sqlite3.connect('db1.db')
cur = con.cursor()
#cur.execute("create table persons(id int, var varchar(50))")
query = "insert into persons values(1,'name1')"
cur.execute(query)
con.commit()
# db_app
# https://github.com/sambapython/python2
# 