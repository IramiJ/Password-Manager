from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QDialog

class popup_window(QDialog):
 def __init__(self, title, placeholder):
  super().__init__()
  self.setFixedSize(300, 210)
  self.setWindowTitle(title)
  self.text_field = QLineEdit(self)
  self.text_field.setPlaceholderText(placeholder)
  self.text_field.returnPressed.connect(self.return_pressed)
  self.exec_()

 def return_pressed(self):
  self.close()
  return self.text_field.text()
 
 
 
  


