from PyQt5.QtWidgets import QMainWindow, QWidget, QTextEdit, QHBoxLayout, QSlider, QVBoxLayout, QLabel
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
 
 def initUI(self): #all of the Main window setups 
  self.setWindowTitle("Password Manager")
  self.setFixedSize(800, 560)
  central_widget = QWidget()

  #Main vertical box layout

  vbox = QVBoxLayout()
  vbox.setContentsMargins(15,15,15,15)
  vbox.setSpacing(20)
  central_widget.setLayout(vbox)
  self.setCentralWidget(central_widget)
  
  #adding buttons to the mainwindow
  

  hbox_top = QHBoxLayout()
  hbox_top.setSpacing(10)

  buttons_top = {
   'Add_button': button(140, 50, "Add ➕",self,add),
   'Delete_button': button(140,50,"Delete 🗑",self,remove),
   'replace_button': button(140,50,"replace ✏",self,replace),
   'view_button': button(140,50,'view specific 👁',self,view_specific),
   'view_all_button': button(140,50,'view all 📜',self,view_all)
  }

  for b in buttons_top:
   hbox_top.addWidget(buttons_top[b])
  
  vbox.addLayout(hbox_top)
 
 #Output Box

  self.output = QTextEdit(self)
  self.output.setReadOnly(True) 
  self.output.setFixedHeight(300)
  vbox.addWidget(self.output)
  
  #Slider

  self.slider = QSlider(Qt.Horizontal, self)
  self.slider.setMinimum(0)
  self.slider.setMaximum(25)
  self.slider.setValue(10)
  self.slider.setFixedWidth(300)
  self.slider.setTickPosition(QSlider.TicksBelow)
  self.slider.setTickInterval(5)
  self.slider_label = QLabel(f"Password length: {self.slider.value()}", self)
  self.slider.valueChanged.connect(lambda value: self.slider_label.setText(f"Password length: {value}"))
  vbox.addWidget(self.slider_label, alignment=Qt.AlignHCenter)
  vbox.addWidget(self.slider, alignment=Qt.AlignHCenter)

  #Bottom Buttons

  hbox_bottom = QHBoxLayout()
  hbox_bottom.setSpacing(15)

  buttons_bottom = {
   'Uppercase_letters': button_bottom(140,50, "Uppercase", self, "Uppercase"),
   'Lowercase_letters': button_bottom(140,50, "Lowercase", self, "Lowercase"),
   'Digits': button_bottom(140,50, "Digits", self, "Digits"),
   'Symbols': button_bottom(140,50, "Symbols", self, "Symbols")
  }
  for btn in buttons_bottom:
   hbox_bottom.addWidget(buttons_bottom[btn])
  
  vbox.addLayout(hbox_bottom)