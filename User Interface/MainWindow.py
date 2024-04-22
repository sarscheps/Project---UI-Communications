import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import QFile, QTextStream
from WeatherApp_ui import Ui_MainWindow
from LinkButton import LinkButton
import os
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # local variables
        self.curr_dir = os.path.dirname(__file__)
        self.homePageMinimumExtension = 260
        self.homePageMaximumExtension = 16777215
        self.logInPanelHidden = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.tempExtendableWidget.hide()
        #self.ui.humidityExtendableWidget.hide()
        self.ui.LogInPanel.hide()

        self.ui.tempLinkButton.clicked.connect(self.on_tempLinkButton_clicked)
        self.ui.humidityLinkButton.clicked.connect(lambda: self.on_humidityLinkButton_clicked)

        self.ui.humidityLinkButton.clicked.connect(self.on_humidityLinkButton_clicked)
        
        # Connect the sidebar buttons to their respective functions --------------------
        self.ui.homePageBtn.clicked.connect(self.on_homePageBtn_clicked)
        self.ui.homePageIconBtn.clicked.connect(self.on_homePageBtn_clicked)

        self.ui.displayModeBtn.clicked.connect(self.on_displayModeBtn_clicked)
        self.ui.displayModeIconBtn.clicked.connect(self.on_displayModeBtn_clicked)
        
        self.ui.syncWithDeviceBtn.clicked.connect(self.on_syncWithDevice_clicked)
        self.ui.syncWithDeviceIconBtn.clicked.connect(self.on_syncWithDevice_clicked)
        # ------------------------------------------------------------------------------
        self.ui.signInBtn.clicked.connect(self.on_signInBtn_clicked)

        self.ui.windowWidget.setCurrentIndex(1)

        # When sidebar btn clicked, shows/hides sidebar
        self.ui.sideBarMenuBtn.toggled.connect(self.on_sideBarMenuBtn_toggled)

        # When profile btn clicked, shows/hides it's respective widget
        self.ui.profileBtn.toggled.connect(self.on_profileBtn_toggled)

        # When sign out btn clicked, takes you to sign in page
        self.ui.signOutBtn.clicked.connect(self.on_signOutBtn_clicked)




#-------------------------------------------------------------------------------------------
    # When Sign Out button is clicked, it takes you to the sign in page
    def on_signOutBtn_clicked(self):
        self.ui.windowWidget.setCurrentIndex(1)

    # When Sign in button is clicked, it takes you to the main screen page
    def on_signInBtn_clicked(self):
        self.ui.windowWidget.setCurrentIndex(0)
        self.ui.sidebarBtnWidget.hide()
    
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
        else:
            self.ui.LogInPanel.hide()
         

        
    def on_tempLinkButton_clicked(self):
        if self.ui.tempLinkButton.extended:
            self.ui.tempLinkButton.extended = False

            #Set the home page to the minium extension when all the buttons are not extended.
            self.ui.homePage.setMaximumHeight(self.homePageMinimumExtension)
            self.ui.tempExtendableWidget.hide()  
            
        else :
            self.ui.tempLinkButton.extended = True
            self.getTempTableData()
            self.ui.tempExtendableWidget.show()
            self.ui.humidityExtendableWidget.hide()

            

            #Reset to the maximum size when extended.
            self.ui.homePage.setMaximumHeight(self.homePageMaximumExtension)


    def on_humidityLinkButton_clicked(self):
        if self.ui.humidityLinkButton.extended:
            self.ui.humidityLinkButton.extended = False

            #Set the home page to the minium extension when all the buttons are not extended.
            self.ui.homePage.setMaximumHeight(self.homePageMinimumExtension)
            self.ui.humidityExtendableWidget.hide()  

        else :
            self.ui.humidityLinkButton.extended = True
            self.ui.humidityExtendableWidget.show()
            self.ui.tempExtendableWidget.hide()

            #Reset to the maximum size when extended..
            self.ui.homePage.setMaximumHeight(self.homePageMaximumExtension)

   
    def getTempTableData(self) -> None:
        with open(os.path.join(self.curr_dir, "data_src/received_data.csv"), newline='') as csvFile:
        # Create a CSV reader object
            print(csvFile.readable)
            csvReader = csv.reader(csvFile)
            
            for index, csvRow in enumerate(csvReader):
                self.ui.tempTableWidget.insertRow(index)
                self.ui.tempTableWidget.setItem(index, column=0, item=QTableWidgetItem(csvRow[0]))
                self.ui.tempTableWidget.setItem(index, column=1, item=QTableWidgetItem(csvRow[1]))

                

   

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
    
    


            
    




