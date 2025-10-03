from PyQt5.QtWidgets import QMainWindow, QWidget

class MainWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.setWindowTitle("Password Manager")
  self.setGeometry(0,0,450,450)
  self.setMaximumHeight(450)
  self.setMaximumWidth(450)
  self.initUI()
 
 def initUI(self):
  central_widget = QWidget()
  self.setCentralWidget(central_widget)