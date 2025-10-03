from PyQt5.QtWidgets import QMainWindow, QWidget

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
  self.setCentralWidget(central_widget)