

## This is not working nor completed. 

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtCore import pyqtSlot, QFile, QTextStream
from sidebar_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.sideBarIconWidget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5,6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    ## Function for changing new page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashboard_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashboard_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    





if __name__ == "__main__":
    app = QApplication(sys.argv)


    ## Loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)


    window = MainWindow()
    window.show()


    sys.exit(app.exec())

