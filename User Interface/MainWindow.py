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
        self.ui.humidityExtendableWidget.hide()
        self.ui.LogInPanel.hide()

        self.ui.tempLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\MoreArrIcon.png"))
        self.ui.humidityLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\MoreArrIcon.png"))
        self.updateTempLastReading()
        self.updateHumidityLastReading()

        self.ui.tempLinkButton.clicked.connect(self.on_tempLinkButton_clicked)
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
         
    def tempLinkButtonExtend(self, extend:bool)->None:
        if extend:
            print("extend")
            self.ui.tempExtendableWidget.show()
            self.ui.tempLinkButton.extended = True
            self.ui.tempLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\LessArrIcon.png"))
        else:
            print("hide")
            self.ui.tempExtendableWidget.hide()
            self.ui.tempLinkButton.extended = False

            self.ui.tempLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\MoreArrIcon.png"))
    
    def humidityLinkButtonExtend(self, extend:bool) ->None:
        if extend:
            self.ui.humidityExtendableWidget.show()
            self.ui.humidityLinkButton.extended = True
            self.ui.humidityLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\LessArrIcon.png"))
        else:
            self.ui.humidityExtendableWidget.hide()
            self.ui.humidityLinkButton.extended = False

            self.ui.humidityLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\MoreArrIcon.png"))

    def on_tempLinkButton_clicked(self):
        if self.ui.tempLinkButton.extended:
            self.tempLinkButtonExtend(False)
            #Set the home page to the minium extension when all the buttons are not extended.
            self.ui.homePage.setMaximumHeight(self.homePageMinimumExtension)

        else :
            self.getTempTableData()
            self.tempLinkButtonExtend(True)
            self.humidityLinkButtonExtend(False)
            
            self.ui.homePage.setMaximumHeight(self.homePageMaximumExtension)
            
        print("test")

    def on_humidityLinkButton_clicked(self):
        if self.ui.humidityLinkButton.extended:
            self.humidityLinkButtonExtend(False)
            #Set the home page to the minium extension when all the buttons are not extended.
            self.ui.homePage.setMaximumHeight(self.homePageMinimumExtension)

        else :
            self.getHumidityTableData()
            self.humidityLinkButtonExtend(True)
            self.tempLinkButtonExtend(False)
            
            self.ui.homePage.setMaximumHeight(self.homePageMaximumExtension)

            
            

   
    def getTempTableData(self) -> None:
        with open(os.path.join(self.curr_dir, "data_src/received_data.csv"),'r', newline='') as csvFile:
        # Create a CSV reader object
            csvReader = csv.reader(csvFile)
            self.ui.tempTableWidget.clear()
            
            for row in range(self.ui.tempTableWidget.rowCount(), 100):
                self.ui.tempTableWidget.insertRow(row)
            
            # Set table headers
            self.ui.tempTableWidget.setHorizontalHeaderLabels(["Timestamp", "Device ID", "Temperature F°"])
            
            index = 0
            for csvRow in reversed(list(csvReader)) :
                if index >= 100:
                    break
                self.ui.tempTableWidget.setItem(index, 0, QTableWidgetItem(csvRow[0]))  # row 1 for time stamp
                self.ui.tempTableWidget.setItem(index, 1, QTableWidgetItem(csvRow[1]))  # row 2 for ID
                self.ui.tempTableWidget.setItem(index, 2, QTableWidgetItem(csvRow[2]))  # row 3 for humidity.
                index +=1
        csvFile.close()


    def getHumidityTableData(self) -> None:
        with open(os.path.join(self.curr_dir, "data_src/received_data.csv"),'r', newline='') as csvFile:
        # Create a CSV reader object
            csvReader = csv.reader(csvFile)
            self.ui.humidityTableWidget.clear()
            
            for row in range(self.ui.humidityTableWidget.rowCount(), 100):
                self.ui.humidityTableWidget.insertRow(row)
            
            # Set table headers
            self.ui.humidityTableWidget.setHorizontalHeaderLabels(["Timestamp", "Device ID", "Humidity %"])
            
            index = 0
            for csvRow in reversed(list(csvReader)):
                if index >= 100:
                    break
                self.ui.humidityTableWidget.setItem(index, 0, QTableWidgetItem(csvRow[0]))   # row 1 for time stamp
                self.ui.humidityTableWidget.setItem(index, 1, QTableWidgetItem(csvRow[1]))   # row 2 for ID   
                self.ui.humidityTableWidget.setItem(index, 2, QTableWidgetItem(csvRow[3]))   # row 3 for humidity.
                index +=1
        csvFile.close()
            

    def updateTempLastReading(self):
        with open(os.path.join(self.curr_dir, "data_src/received_data.csv"),'r', newline='') as csvFile:
        # Create a CSV reader object
            csvReader = csv.reader(csvFile)
            
            # Skip the first row
            next(csvReader)

            for csvRow in reversed(list(csvReader)):
                lastReading = csvRow[2] + " F°"
                self.ui.tempLinkButton.set_label_text(lastReading)
            csvFile.close()

    def updateHumidityLastReading(self):
        with open(os.path.join(self.curr_dir, "data_src/received_data.csv"),'r', newline='') as csvFile:
        # Create a CSV reader object
            csvReader = csv.reader(csvFile)
            
            # Skip the first row
            next(csvReader)
            
            for csvRow in reversed(list(csvReader)):
                lastReading = csvRow[3] + "%"
                self.ui.humidityLinkButton.set_label_text(lastReading)
            csvFile.close()
                

    
        


            
    




