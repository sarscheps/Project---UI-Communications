
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget
from PyQt6.QtCore import QFile, QTextStream
from WeatherApp_ui import Ui_MainWindow
from LinkButton import LinkButton


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.tempExtendableWidget.hide()
        self.ui.humidityExtendableWidget.hide()
        self.ui.LogInPanel.hide()

        self.ui.tempLinkButton.clicked.connect(lambda: self.on_linkButton_clicked(self.ui.tempLinkButton, self.ui.tempExtendableWidget))
        self.ui.humidityLinkButton.clicked.connect(lambda: self.on_linkButton_clicked(self.ui.humidityLinkButton, self.ui.humidityExtendableWidget))
        self.ui.profileBtn.clicked.connect(lambda:self.on_profileButton_clicked())


    
    def on_linkButton_clicked(self,linkButton:LinkButton, extendableWidget:QTableWidget):
        if linkButton.extended:
            linkButton.extended = False
            extendableWidget.hide()  
            
        else :
            linkButton.extended = True
            extendableWidget.show()


    def on_profileButton_clicked(self):
        self.ui.LogInPanel.show()
        self.ui.LogInPanel.raise_()

    '''   
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
    '''
    
    


            
    




