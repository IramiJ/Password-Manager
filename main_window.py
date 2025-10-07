from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QTextEdit, QHBoxLayout, QSlider
from PyQt5.QtCore import Qt
from Button import button, button_bottom
from database.database import *

class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.Uppercase = True
  self.Lowercase = True
  self.Digits = True
  self.Symbols = True
  self.initUI()
 
 def initUI(self):
  #all of the Main window setups
  self.setWindowTitle("Password Manager")
  self.setFixedSize(800, 560)
  central_widget = QWidget()
  grid = QGridLayout()
  grid.setContentsMargins(0, 0, 0, 0)
  grid.setSpacing(0)
  grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
  central_widget.setLayout(grid)
  self.setCentralWidget(central_widget)
  #adding buttons to the mainwindow
  self.output = QTextEdit(self)
  self.output.setReadOnly(True)
  buttons_top = {
   'Add_button': button(160, 50, "Add password",self,add),
   'Delete_button': button(160,50,"Delete password",self,remove),
   'replace_button': button(160,50,"replace existing password",self,replace),
   'view_button': button(160,50,'view specific password',self,view_specific),
   'view_all_button': button(160,50,'view all passwords',self,view_all)
  }
 
  hbox = QHBoxLayout()

  buttons_bottom = {
   'Uppercase_letters': button_bottom(160,50, f"Including Uppercase({self.Uppercase})", self, "Uppercase"),
   'Lowercase_letters': button_bottom(160,50, f"Including Lowercase({self.Lowercase})", self, "Lowercase"),
   'Digits': button_bottom(160,50, f"Including Digits({self.Digits})", self, "Digits"),
   'Symbols': button_bottom(160,50, f"Including Symbols({self.Symbols})", self, "Symbols")
  }
  for btn in buttons_bottom:
   hbox.addWidget(buttons_bottom[btn])
  
  i = 0
  for b in buttons_top:
   grid.addWidget(buttons_top[b],0,i)
   i+=1

  self.slider = QSlider(Qt.Horizontal, self)
  self.slider.setMinimum(1)
  self.slider.setMaximum(25)
  self.slider.setValue(10)

  #adding the output of dat
  grid.addWidget(self.output)
  self.output.setFixedSize(800, 300)
  grid.addWidget(self.slider, 2, 2, 1, 2)
  grid.addLayout(hbox,grid.rowCount(),0,1,grid.columnCount(),alignment=Qt.AlignRight | Qt.AlignBottom)

  

  
  
  

