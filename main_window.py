from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from Button import button
from database.database import view_all
from database.database import *

class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.initUI()

 def initUI(self):
  self.setWindowTitle("Password Manager")
  self.setGeometry(0,0,800,560)
  self.setMaximumHeight(560)
  self.setMaximumWidth(800)
  central_widget = QWidget()
  grid = QGridLayout()
  grid.setContentsMargins(0, 0, 0, 0)
  grid.setSpacing(0)
  grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
  central_widget.setLayout(grid)
  self.setCentralWidget(central_widget)
  #added a test button to see if everything works
  buttons = {
   'Add_button': button(160, 50, "Add password",self,add),
   'Delete_button': button(160,50,"Delete password",self,remove),
   'replace_button': button(160,50,"replace existing password",self,replace),
   'view_button': button(160,50,'view specific password',self,view_specific),
   'view_all_button': button(160,50,'view all passwords',self,view_all)
  }
  i = 0
  for b in buttons:
   grid.addWidget(buttons[b],0,i)
   i+=1
