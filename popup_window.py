from PyQt5.QtWidgets import (
 QLineEdit, QDialog, QVBoxLayout, QLabel, QDialogButtonBox
)
from PyQt5.QtCore import Qt

class popup_window(QDialog):
 def __init__(self, title, placeholder):
  super().__init__()
  self.setFixedSize(350, 200)
  self.setWindowTitle(title)

  #Layout
  layout = QVBoxLayout()
  layout.setContentsMargins(20, 20, 20, 20)
  layout.setSpacing(15)
  self.setLayout(layout)

  #Title Label
  label = QLabel(title, self)
  label.setAlignment(Qt.AlignCenter)
  label.setStyleSheet("font-size: 14pt; font-weight: bold; color: #f0f0f0;")
  layout.addWidget(label)

  #Input field
  self.text_field = QLineEdit(self)
  self.text_field.setPlaceholderText(placeholder)
  self.text_field.setStyleSheet("""
   QLineEdit {
    background-color: #3c3f41;
    color: #ffffff;
    border: 1px solid #666;
    border-radius: 6px;
    padding: 6px;
   }
   QLineEdit:focus {
    border: 1px solid #007acc;
   }
  """)
  layout.addWidget(self.text_field)

  #Buttons (OK / Cancel)
  button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
  button_box.accepted.connect(self.accept)
  button_box.rejected.connect(self.reject)
  layout.addWidget(button_box)

  #Run dialog
  self.text_field.returnPressed.connect(self.accept)
  self.exec_()

 def get_text(self):
  return self.text_field.text().strip()
 
 
 
  


