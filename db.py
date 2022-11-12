import sqlite3
 
print("Create a todo list database...")
 
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE todo (category char(50), theitem char(100),id INTEGER PRIMARY KEY )")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','eggs')")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','milk')")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','bread')")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Activities','snow tires')")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Activities','rake lawn')")
conn.commit()
 
print("Database todo.db created")

