

## This is not working nor completed. 
import sys
from PyQt6. import QMainWindow, QApplication, QPushButton
from MainWindow import MainWindow


if __name__ == "__main__": 
    app = QApplication(sys.argv)


    ## Loading style file
    #with open("style.qss", "r") as style_file:
    #   style_str = style_file.read()
    #app.setStyleSheet(style_str)


    window = MainWindow()
    window.show()


    sys.exit(app.exec())

