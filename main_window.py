from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton
from Button import button



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
  central_widget.setLayout(grid)
  self.setCentralWidget(central_widget)
#  buttons = [button(50,50,self)]  added a test button to see if everything works