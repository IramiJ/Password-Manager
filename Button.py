from PyQt5.QtWidgets import QPushButton
class button(QPushButton):
 def __init__(self, width, height, text, mainwindow, func):
  super().__init__(text, mainwindow)
  self.setFixedSize(width, height)
  self.clicked.connect(func)