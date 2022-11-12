#I got started on this project by following a tutorial here  https://funprojects.blog/tag/sqlite/

# Build a Todo List 
#
import sqlite3
from bottle import route, run, template, request, redirect, post  

# The main page shows the Todo list, /new and /delete references are called from this page
@route('/')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM todo order by category,theitem ")
    result = c.fetchall()
    # in case column names are required
    colnames = [description[0] for description in c.description]
    numcol = len(colnames)
    # for now only the rows=result variables are used
    output = template('show_todo', rows=result, headings=colnames, numcol = numcol)
    return output

# Add new items into the database
@route('/new', method='POST')
def new_item():

    print("New Post:", request.body.read())
    theitem = request.forms.get("theitem")
    newcategory = request.forms.get("newcategory")

    if theitem != "":        
        
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (category,theitem) VALUES (?,?)", (newcategory,theitem))
        conn.commit()
        c.close()

    redirect("/") # go back to the main page   

# Delete an item in the database
@route('/delete', method='POST')
def delete_item():

    print("Delete:", request.body.read() )
    theid = request.forms.get("delitem").strip()
    print("theid: ", theid)
               
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    sqlstr = "DELETE FROM todo WHERE id=" + str(theid)
    print(sqlstr)
    c.execute(sqlstr)
    conn.commit()
    c.close()

    redirect("/") # go back to the main page   

#add a due date to the task in the database
@route('/due_date', method='POST')
def due_date():

    print("Update:", request.body.read() )
    theid = request.forms.get("id").strip()
    print("theid: ", theid)
    theid = str(theid)
    new_due_date = request.forms.get("new_due_date")
               
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    sqlstr = "UPDATE todo SET due_date= '" +(new_due_date)+ "' WHERE id=" +(theid)
    print(sqlstr)
    c.execute(sqlstr)
    conn.commit()
    c.close()

    redirect("/") # go back to the main page   

#add a person in charge of a task to the database
@route('/person_in_charge', method='POST')
def person_in_charge():

    print("Update:", request.body.read() )
    theid = request.forms.get("id").strip()
    print("theid: ", theid)
    theid = str(theid)
    new_person_in_charge = request.forms.get("new_person_in_charge")
               
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    sqlstr = "UPDATE todo SET person_in_charge= '" +(new_person_in_charge)+ "' WHERE id=" +(theid)
    print(sqlstr)
    c.execute(sqlstr)
    conn.commit()
    c.close()

    redirect("/") # go back to the main page  
        
run(reloader = True)