import sqlite3


conn = sqlite3.connect('data1.db')
c = conn.cursor()

user = (1, 'bob', 'abcd')

create_query = "CREATE TABLE users (id int, username text, password text)"
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
select_query = "SELECT * FROM users"

c.execute(create_query)
c.execute(insert_query, user)

users = [
    (2, 'hitesh', 'bkc'),
    (3, 'anita', 'cdb')
]

c.executemany(insert_query, users)
for user in c.execute(select_query):
    print user

conn.commit()
conn.close()


