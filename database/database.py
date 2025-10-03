import sqlite3



def add(app_name, password): # adds a new password to the table 
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 cursor.execute("INSERT INTO passwords VALUES (?, ?) ", (app_name, password))
 connection.commit()

def remove(app_name): # removes a certain password from the table
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 cursor.execute("DELETE FROM passwords WHERE app_name = ?", (app_name, ))
 connection.commit()

def replace(app_name, password): # allows you to update your password, finding it by app_name
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 cursor.execute("UPDATE passwords SET password = (?) WHERE app_name = (?)", (password, app_name))
 connection.commit()

def view_specific(app_name): # allows you to view a specific password, finding it by app_name
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 cursor.execute("SELECT password FROM passwords WHERE app_name = (?)", (app_name, ))
 all = cursor.fetchall()[0][0]
 return all

def view_all(): # shows all of the entrys within the database
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 cursor.execute("SELECT * FROM passwords")
 all = cursor.fetchall()
 print(all)
 return all
