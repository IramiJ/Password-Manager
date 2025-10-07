import sqlite3
from popup_window import popup_window
from password_generator import generate_password

def add(mainwindow): # adds a new password to the table 
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 p1 = popup_window("Enter App Name", "pleace enter your app name")
 app_name = p1.text_field.text()
 password = generate_password(mainwindow.Uppercase, mainwindow.Lowercase, mainwindow.Digits, mainwindow.Symbols, mainwindow.slider.value())
 cursor.execute("INSERT INTO passwords VALUES (?, ?) ", (app_name, password))
 connection.commit()

def remove(mainwindow): # removes a certain password from the table
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 p1 = popup_window("Enter App Name", "please enter your app name")
 app_name = p1.text_field.text()
 cursor.execute("DELETE FROM passwords WHERE app_name = ?", (app_name, ))
 connection.commit()

def replace(mainwindow): # allows you to update your password, finding it by app_name
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 p = popup_window("Enter App Name", "please enter your app name")
 app_name = p.text_field.text()
 password = generate_password(mainwindow.Uppercase, mainwindow.Lowercase, mainwindow.Digits, mainwindow.Symbols, mainwindow.slider.value())
 cursor.execute("UPDATE passwords SET password = (?) WHERE app_name = (?)", (password, app_name))
 connection.commit()

def view_specific(mainwindow): # allows you to view a specific password, finding it by app_name
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 p = popup_window("Enter App Name", "please enter your App Name")
 app_name = p.text_field.text()
 cursor.execute("SELECT password FROM passwords WHERE app_name = (?)", (app_name, ))
 try:
  all = cursor.fetchall()[0][0]
 except(IndexError):
  all = ''
 mainwindow.output.setPlainText(all)


def view_all(mainwindow): # shows all of the entrys within the database
 connection = sqlite3.connect('database/test.db')
 cursor = connection.cursor()
 cursor.execute("SELECT * FROM passwords")
 all = cursor.fetchall()
 string = ""
 for password in all:
  string += password[0] + ": " + password[1] + "; \n"
 mainwindow.output.setPlainText(string)
