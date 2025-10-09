import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow



def main():
 app = QApplication(sys.argv)
 dark_stylesheet = """
QMainWindow {
    background-color: #2b2b2b;
    color: #f0f0f0;
}

QTextEdit {
    background-color: #3c3f41;
    color: #ffffff;
    border: 1px solid #555;
    selection-background-color: #007acc;
    font-family: Consolas, monospace;
}

QPushButton {
    background-color: #444;
    color: #f0f0f0;
    border: 1px solid #666;
    border-radius: 6px;
    padding: 6px;
}
QPushButton:hover {
    background-color: #555;
}
QPushButton:pressed {
    background-color: #007acc;
}

QSlider::groove:horizontal {
    border: 1px solid #444;
    height: 6px;
    background: #3c3f41;
    margin: 0px;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background: #007acc;
    border: 1px solid #007acc;
    width: 14px;
    height: 14px;
    margin: -5px 0;
    border-radius: 7px;
}
QSlider::sub-page:horizontal {
    background: #007acc;
}
"""

 app.setStyleSheet(dark_stylesheet)
 window = MainWindow()
 window.show()
 sys.exit(app.exec_())

if __name__ == '__main__':
 main()