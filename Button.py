from PyQt5.QtWidgets import QPushButton
class button(QPushButton):
 def __init__(self, width, height, text, mainwindow, func):
  super().__init__(text, mainwindow)
  self.setFixedSize(width, height)
  self.clicked.connect(lambda: func(mainwindow))

class button_bottom(QPushButton):
 def __init__(self, width, height, label, mainwindow, attr_name):
  super().__init__(label, mainwindow)
  self.setFixedSize(width, height)
  self.mainwindow = mainwindow
  self.attr_name = attr_name
  self.clicked.connect(self.flip_and_update)

 def flip_and_update(self):
  # flip the value
  current = getattr(self.mainwindow, self.attr_name)
  setattr(self.mainwindow, self.attr_name, not current)
  self.setText(f"Including {self.attr_name} ({getattr(self.mainwindow, self.attr_name)})")
