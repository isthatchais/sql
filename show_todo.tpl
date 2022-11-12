%#Main template - show Todo list, with delete and add item functionality
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>

<h1>To do List</h1>
<p>Build with Python using Bottle and SQLite</p>
<table>
    % setdefault('icategory', '')
        <tr>
            <th>Category</th>
            <th>Task</th>
            <th>Due Date</th>
            <th>Person in Charge</th>
            <th>Delete</th>
        </tr>

    %for row in rows:
    %
            <tr>
                <td> 
                    {{row[0]}}
                </td>
                <td> 
                    {{row[1]}} 
                </td>

                <form action="/due_date" method="post">
                <td> 
                    <input type="text" name ="new_due_date" value=" {{row[3]}}  ">
                    <button type="submit" name="id" value=' {{row[2]}} '>Update</button>
                </td>
                </form>
                <form action="/person_in_charge" method="post">
                <td> 
                    <input type="text" name ="new_person_in_charge" value=" {{row[4]}} ">
                    <button type="submit" name="id" value=" {{row[2]}} ">Update</button>
                </td>
                </form>
                %# Add a botton after the item with the item's unique ID
                <form action="/delete" method="post">
                <td>
                    <button type="submit" name="delitem" value=' {{row[2]}} '>Delete</button>
                </td>
                </form>
            </tr>

    %end
</table>
<hr>

%#template form for a new task
<p>Add a new task to the ToDo list: </p>
<form action="/new" method="POST">
    <select name = "newcategory">
        <option value="Activities">Activities</option>
        <option value="Projects">Projects</option>
        <option value="Shopping" selected>Shopping</option>
    </select>
    <input type="text" size="25" name ="theitem">
    <input type="submit" name="save" value="save">
</form>