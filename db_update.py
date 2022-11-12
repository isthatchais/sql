#updae as of 11/5 to add in due date and person in charge

import sqlite3
 
print("Update todo database...")
 
conn = sqlite3.connect('todo.db') 
conn.execute("ALTER TABLE todo ADD due_date char(50)")
conn.execute("ALTER TABLE todo ADD person_in_charge char(50)")

conn.commit()
 
print("Database todo.db updated")