
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
        self.logInPanelHidden = False
        
        self.ui.tempExtendableWidget.hide()
        self.ui.humidityExtendableWidget.hide()
        #self.ui.LogInPanel.hide()

        self.ui.tempLinkButton.clicked.connect(lambda: self.on_linkButton_clicked(self.ui.tempLinkButton, self.ui.tempExtendableWidget))
        self.ui.humidityLinkButton.clicked.connect(lambda: self.on_linkButton_clicked(self.ui.humidityLinkButton, self.ui.humidityExtendableWidget))
        self.ui.profileBtn.clicked.connect(lambda:self.on_profileBtn_clicked)

              
        #self.ui.homePageBtn.setChecked(True)

        # Connect the buttons to their respective functions
        self.ui.homePageBtn.clicked.connect(self.on_homePageBtn_clicked)
        self.ui.homePageIconBtn.clicked.connect(self.on_homePageBtn_clicked)

        self.ui.displayModeBtn.clicked.connect(self.on_displayModeBtn_clicked)
        self.ui.displayModeIconBtn.clicked.connect(self.on_displayModeBtn_clicked)
        
        self.ui.syncWithDeviceBtn.clicked.connect(self.on_syncWithDevice_clicked)
        self.ui.syncWithDeviceIconBtn.clicked.connect(self.on_syncWithDevice_clicked)
        self.ui.signInBtn.clicked.connect(self.on_signInBtn_clicked)

        self.ui.windowWidget.setCurrentIndex(1)

        #self.ui.signInBtn.clicked.connect(self.showSignInPage)
        #self.ui.signUpBtn.clicked.connect(self.showSignUpPage)
    
    def on_signInBtn_clicked(self):
        self.ui.windowWidget.setCurrentIndex(0)
        self.ui.sidebarBtnWidget.hide()  


    def on_homePageBtn_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(0)

    def on_displayModeBtn_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(1)

    def on_syncWithDevice_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(2)

    #def showSignInPage(self):
    #   self.ui.windowWidget.setCurrentIndex(1)

    #def showSignUpPage(self):
    #    self.ui.windowWidget.setCurrentIndex(2)
    
    #def showMainScreenPage(self):
    #    self.ui.windowWidget.setCurrentIndex(0)

    def on_profileBtn_clicked(self):
        if self.logInPanelHidden:
            self.ui.LogInPanel.setVisible(True)
            self.logInPanelHidden = False
        else:
            self.ui.LogInPanel.setVisible(False)
            self.logInPanelHidden = True
        

    def on_linkButton_clicked(self,linkButton:LinkButton, extendableWidget:QTableWidget):
        if linkButton.extended:
            linkButton.extended = False
            extendableWidget.hide()  
            
        else :
            linkButton.extended = True
            extendableWidget.show()


   

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
    
    


            
    




