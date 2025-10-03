import sys, random
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget


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

def main():
 app = QApplication(sys.argv)
 window = MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == '__main__':
 main()