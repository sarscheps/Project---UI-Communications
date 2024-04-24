import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import QFile, QTextStream, Qt
from PyQt6.QtGui import QColor
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas ## backend_qt6agg
from datetime import datetime
from WeatherApp_ui import Ui_MainWindow
from LinkButton import LinkButton
import os
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # local variables
        self.curr_dir = os.path.dirname(__file__)
        self.homePageMinimumExtension = 16777215
        self.homePageMaximumExtension = 16777215

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.tempExtendableWidget.hide()
        self.ui.humidityExtendableWidget.hide()
        self.ui.logInPanelLine.hide()
        self.ui.LogInPanel.hide()

        self.ui.windowWidget.setCurrentIndex(1)
        self.updateTempLastReading()
        self.updateHumidityLastReading()
        self.ui.ScrollAreaWidget.setMaximumHeight(self.homePageMinimumExtension)

        #homePageSpacers = [self.ui.homePage..itemAt(i) for i in range(layout.count()) if layout.itemAt(i).spacerItem()]

        self.ui.tempLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\MoreArrIcon.png"))
        self.ui.humidityLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\MoreArrIcon.png"))

        self.ui.humidityTableWidget.horizontalHeader().setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
            "background-color: rgb(0, 160, 220);\n"
            "border-color: rgb(0, 0, 0);")
        self.ui.tempTableWidget.horizontalHeader().setStyleSheet("font: 700 9pt \"Segoe UI\";\n"
            "background-color: rgb(0, 160, 220);\n"
            "border-color: rgb(0, 0, 0);")
        

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

        self.ui.tempPlotBushButton.toggled.connect(self.on_tempPlotBushButton_toggled)

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

#-------------------------------------------------------------------------------------------
    # When Sign in button is clicked, it takes you to the main screen page
    def on_signInBtn_clicked(self):
        self.ui.windowWidget.setCurrentIndex(0)
        self.ui.sidebarBtnWidget.hide()

#-------------------------------------------------------------------------------------------
    # When sidebar btn clicked, shows/hides sidebar
    def on_sideBarMenuBtn_toggled(self, checked):
        if checked:
            self.ui.iconOnlyWidget.hide()
            self.ui.sidebarBtnWidget.show()
        else: 
            self.ui.sidebarBtnWidget.hide()
            self.ui.iconOnlyWidget.show()

#-------------------------------------------------------------------------------------------
    # Sets current page to the home page
    def on_homePageBtn_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(0)

#-------------------------------------------------------------------------------------------
    # Sets current page to the display mode page
    def on_displayModeBtn_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(1)

#-------------------------------------------------------------------------------------------
    # Sets current page to the sync with device page
    def on_syncWithDevice_clicked(self):
        self.ui.pagesWidget.setCurrentIndex(2)

#-------------------------------------------------------------------------------------------
    # Toggles the visibility of the login panel
    def on_profileBtn_toggled(self, checked):
        if checked:
            self.ui.LogInPanel.show()
            self.ui.logInPanelLine.show()
        else:
            self.ui.LogInPanel.hide()
            self.ui.logInPanelLine.hide()

#-------------------------------------------------------------------------------------------
    # Extends or collapses the temperature link button
    def tempLinkButtonExtend(self, extend:bool)->None:
        if extend:
            self.ui.tempExtendableWidget.show()
            self.ui.tempLinkButton.extended = True
            self.ui.tempLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\LessArrIcon.png"))
        else:
            self.ui.tempExtendableWidget.hide()
            self.ui.tempLinkButton.extended = False

            self.ui.tempLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\MoreArrIcon.png"))

    #-------------------------------------------------------------------------------------------
    # Extends or collapses the humidity link button
    def humidityLinkButtonExtend(self, extend:bool) ->None:
        if extend:
            self.ui.humidityExtendableWidget.show()
            self.ui.humidityLinkButton.extended = True
            self.ui.humidityLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\LessArrIcon.png"))
        else:
            self.ui.humidityExtendableWidget.hide()
            self.ui.humidityLinkButton.extended = False

            self.ui.humidityLinkButton.set_arrow_icon(os.path.join(self.curr_dir, "icons\BasicIcons\MoreArrIcon.png"))

#-------------------------------------------------------------------------------------------
    # Handles the click event of the temperature link button
    def on_tempLinkButton_clicked(self):
        if self.ui.tempLinkButton.extended:
            self.tempLinkButtonExtend(False)
            # Set the home page to the minimum extension when all the buttons are not extended.
            self.ui.ScrollAreaWidget.setMaximumHeight(self.homePageMinimumExtension)
        else :
            self.getTempTableData()
            self.tempLinkButtonExtend(True)
            self.humidityLinkButtonExtend(False)
            
            self.ui.ScrollAreaWidget.setMaximumHeight(self.homePageMaximumExtension)
        
    #-------------------------------------------------------------------------------------------
    # Handles the click event of the humidity link button
    def on_humidityLinkButton_clicked(self):
        if self.ui.humidityLinkButton.extended:
            self.humidityLinkButtonExtend(False)
            # Set the home page to the minimum extension when all the buttons are not extended.
            self.ui.ScrollAreaWidget.setMaximumHeight(self.homePageMinimumExtension)
        else :
            self.getHumidityTableData()
            self.humidityLinkButtonExtend(True)
            self.tempLinkButtonExtend(False)
            
            self.ui.ScrollAreaWidget.setMaximumHeight(self.homePageMaximumExtension)

#-------------------------------------------------------------------------------------------
    # Retrieves data for the temperature table
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

#-------------------------------------------------------------------------------------------
    # Retrieves data for the humidity table
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
            
#-------------------------------------------------------------------------------------------
    # Updates the text of the temperature link button with the last reading
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

#-------------------------------------------------------------------------------------------
    # Updates the text of the humidity link button with the last reading
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
            

#-------------------------------------------------------------------------------------------
    def on_tempPlotBushButton_toggled(self,checked):
        if checked:
            self.tempPlotData()
            self.ui.tempStackedWidget.setCurrentIndex(1) 
            self.ui.tempExtendableWidget.setMaximumHeight(450)
        else:
            self.ui.tempStackedWidget.setCurrentIndex(0)
            self.ui.tempExtendableWidget.setMaximumHeight(260)
            

    def tempPlotData(self):
        for i in reversed(range(self.ui.tempPlotPageLayout.count())):
            widget = self.ui.tempPlotPageLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Load data from CSV file
        csvData = {"x": [], "y": []}
        with open(os.path.join(self.curr_dir, "data_src/received_data.csv"),'r', newline='') as csvFile:
            csvReader = csv.DictReader(csvFile)
            for row in csvReader:
                print(row)
                x_value = datetime.strptime(row['Timestamp '], "%m/%d/%Y %H:%M")  # Adjust the format according to your CSV
                csvData["x"].append(x_value)
                csvData["y"].append(float(row['Temperature']))  # Convert y value to integer
        
            csvFile.close()
        
        # Create a plot
        figure, axis = plt.subplots()

        axis.plot(csvData["x"], csvData["y"])

        # Set x-axis label rotation to 0 degrees (horizontal)
        plt.xticks(rotation=20)
        
        # Create a canvas for the plot
        canvas = FigureCanvas(figure)
        
        
       # Set the alignment of the canvas to the top
        self.ui.tempPlotPageLayout.addWidget(canvas, alignment=Qt.AlignmentFlag.AlignTop)
        
    




