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
  self.setCheckable(True)

  self.mainwindow = mainwindow
  self.attr_name = attr_name

  # set initial state from mainwindow
  self.setChecked(getattr(self.mainwindow, self.attr_name))

  # sync button state with flag
  self.toggled.connect(self.update_flag)

  # style for normal/toggled states
  self.setStyleSheet("""
            QPushButton {
                background-color: #444;
                color: #fff;
                border: 1px solid #666;
                border-radius: 6px;
                padding: 6px;
            }
            QPushButton:checked {
                background-color: #007acc;
                border: 1px solid #005f99;
            }
        """)

 def update_flag(self, state):
  setattr(self.mainwindow, self.attr_name, state)
