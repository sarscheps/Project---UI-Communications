## This is not working nor completed. 
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from WeatherApp_ui import Ui_MainWindow

# Function for changing page to user page
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()    

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.iconOnlyWidget.hide()
        self.ui.pagesWidget.setCurrentIndex(0)
        self.ui.homePageBtn.setChecked(True)

        # Connect the buttons to their respective functions
        self.ui.homePageBtn.clicked.connect(self.showHomePage)
        self.ui.homePageIconBtn.clicked.connect(self.showHomePage)

        self.ui.displayModeBtn.clicked.connect(self.showDisplayModePage)
        self.ui.displayModeIconBtn.clicked.connect(self.showDisplayModePage)
        
        self.ui.syncWithDeviceBtn.clicked.connect(self.showSyncWithDevicePage)
        self.ui.syncWithDeviceIconBtn.clicked.connect(self.showSyncWithDevicePage)
        
    def showHomePage(self):
        self.ui.pagesWidget.setCurrentIndex(0)

    def showDisplayModePage(self):
        self.ui.pagesWidget.setCurrentIndex(1)

    def showSyncWithDevicePage(self):
        self.ui.pagesWidget.setCurrentIndex(2)




if __name__ == "__main__":
    app = QApplication(sys.argv)


    ## Loading style file
    #with open("style.qss", "r") as style_file:
    #   style_str = style_file.read()
    #app.setStyleSheet(style_str)


    window = MainWindow()
    window.show()




    sys.exit(app.exec())

