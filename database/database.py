import sqlite3
from popup_window import popup_window
from password_generator import generate_password

def add(): # adds a new password to the table 
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 p1 = popup_window("Enter App Name", "pleace enter your app name")
 app_name = p1.text_field.text()
 password = generate_password(length=20)
 cursor.execute("INSERT INTO passwords VALUES (?, ?) ", (app_name, password))
 connection.commit()

def remove(): # removes a certain password from the table
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 p1 = popup_window("Enter App Name", "please enter your app name")
 app_name = p1.text_field.text()
 cursor.execute("DELETE FROM passwords WHERE app_name = ?", (app_name, ))
 connection.commit()

def replace(): # allows you to update your password, finding it by app_name
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 p = popup_window("Enter App Name", "please enter your app name")
 app_name = p.text_field.text()
 password = generate_password(lenght=20)
 cursor.execute("UPDATE passwords SET password = (?) WHERE app_name = (?)", (password, app_name))
 connection.commit()

def view_specific(app_name): # allows you to view a specific password, finding it by app_name
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 p = popup_window("Enter App Name", "please enter your App Name")
 app_name = p.text_field.text()
 cursor.execute("SELECT password FROM passwords WHERE app_name = (?)", (app_name, ))
 all = cursor.fetchall()[0][0]
 print(all)
 return all

def view_all(): # shows all of the entrys within the database
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 cursor.execute("SELECT * FROM passwords")
 all = cursor.fetchall()
 print(all)
 return all
