## This is not working nor completed. 
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

    ## Loading style file
    #with open("style.qss", "r") as style_file:
    #   style_str = style_file.read()
    #app.setStyleSheet(style_str)