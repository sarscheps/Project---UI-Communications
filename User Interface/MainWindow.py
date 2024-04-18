
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
        self.ui.LogInPanel.hide()

        self.ui.tempLinkButton.clicked.connect(lambda: self.on_linkButton_clicked(self.ui.tempLinkButton, self.ui.tempExtendableWidget))
        self.ui.humidityLinkButton.clicked.connect(lambda: self.on_linkButton_clicked(self.ui.humidityLinkButton, self.ui.humidityExtendableWidget))
        
        

              
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

        # When sidebar btn clicked, shows/hides sidebar
        self.ui.sideBarMenuBtn.toggled.connect(self.on_sideBarMenuBtn_toggled)

        # When profile btn clicked, shows/hides it's respective widget
        self.ui.profileBtn.toggled.connect(self.on_profileBtn_toggled)

        #self.ui.signInBtn.clicked.connect(self.showSignInPage)
        #self.ui.signUpBtn.clicked.connect(self.showSignUpPage)
    
    # When Sign in button is clicked, it takes you to the main screen page
    def on_signInBtn_clicked(self):
        self.ui.windowWidget.setCurrentIndex(0)
        self.ui.sidebarBtnWidget.hide()  

    # Add function: When Sign out button is clicked, it takes you to the Sign In page
    
    # When sidebar btn clicked, shows/hides sidebar
    def on_sideBarMenuBtn_toggled(self, checked):
        if checked:
            self.ui.iconOnlyWidget.hide()
            self.ui.sidebarBtnWidget.show()
        else: 
            self.ui.sidebarBtnWidget.hide()
            self.ui.iconOnlyWidget.show()


    def on_homePageBtn_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(0)

    def on_displayModeBtn_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(1)

    def on_syncWithDevice_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(2)

    def on_profileBtn_toggled(self, checked):
        if checked:
            self.ui.LogInPanel.show()
            #self.ui.accountInfoWidget.show()
            #self.ui.deviceInfoWidget.show()
            #self.ui.signOutBtn.show()  
        else:
            self.ui.LogInPanel.hide()
            #self.ui.accountInfoWidget.hide()
            #self.ui.deviceInfoWidget.hide()
            #self.ui.signOutBtn.hide()
         

        

    def on_linkButton_clicked(self,linkButton:LinkButton, extendableWidget:QTableWidget):
        print("clicked")
        if linkButton.extended:
            linkButton.extended = False
            extendableWidget.hide()  
            
        else :
            linkButton.extended = True
            extendableWidget.show()


    #def showSignInPage(self):
    #   self.ui.windowWidget.setCurrentIndex(1)

    #def showSignUpPage(self):
    #    self.ui.windowWidget.setCurrentIndex(2)
    
    #def showMainScreenPage(self):
    #    self.ui.windowWidget.setCurrentIndex(0)

   

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
    
    


            
    




