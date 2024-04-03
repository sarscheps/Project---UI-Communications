# Form implementation generated from reading ui file '.\sidebar_v2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 575)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.sideBarIconWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.sideBarIconWidget.setObjectName("sideBarIconWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sideBarIconWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.exitBtn = QtWidgets.QPushButton(parent=self.sideBarIconWidget)
        self.exitBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/exit_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exitBtn.setIcon(icon)
        self.exitBtn.setIconSize(QtCore.QSize(20, 20))
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout_4.addWidget(self.exitBtn)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.homePageIconBtn = QtWidgets.QPushButton(parent=self.sideBarIconWidget)
        self.homePageIconBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/homePage_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homePageIconBtn.setIcon(icon1)
        self.homePageIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.homePageIconBtn.setCheckable(True)
        self.homePageIconBtn.setAutoExclusive(True)
        self.homePageIconBtn.setObjectName("homePageIconBtn")
        self.verticalLayout_3.addWidget(self.homePageIconBtn)
        self.displayModeIconBtn = QtWidgets.QPushButton(parent=self.sideBarIconWidget)
        self.displayModeIconBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/displayMode_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.displayModeIconBtn.setIcon(icon2)
        self.displayModeIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.displayModeIconBtn.setCheckable(True)
        self.displayModeIconBtn.setAutoExclusive(True)
        self.displayModeIconBtn.setObjectName("displayModeIconBtn")
        self.verticalLayout_3.addWidget(self.displayModeIconBtn)
        self.syncWithDeviceIconBtn = QtWidgets.QPushButton(parent=self.sideBarIconWidget)
        self.syncWithDeviceIconBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/syncWithDevice_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.syncWithDeviceIconBtn.setIcon(icon3)
        self.syncWithDeviceIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.syncWithDeviceIconBtn.setCheckable(True)
        self.syncWithDeviceIconBtn.setAutoExclusive(True)
        self.syncWithDeviceIconBtn.setObjectName("syncWithDeviceIconBtn")
        self.verticalLayout_3.addWidget(self.syncWithDeviceIconBtn)
        self.searchByAreaIconBtn = QtWidgets.QPushButton(parent=self.sideBarIconWidget)
        self.searchByAreaIconBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/searchByArea_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.searchByAreaIconBtn.setIcon(icon4)
        self.searchByAreaIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.searchByAreaIconBtn.setCheckable(True)
        self.searchByAreaIconBtn.setAutoExclusive(True)
        self.searchByAreaIconBtn.setObjectName("searchByAreaIconBtn")
        self.verticalLayout_3.addWidget(self.searchByAreaIconBtn)
        self.savedLocationsIconBtn = QtWidgets.QPushButton(parent=self.sideBarIconWidget)
        self.savedLocationsIconBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/savedLocations_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.savedLocationsIconBtn.setIcon(icon5)
        self.savedLocationsIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.savedLocationsIconBtn.setCheckable(True)
        self.savedLocationsIconBtn.setAutoExclusive(True)
        self.savedLocationsIconBtn.setObjectName("savedLocationsIconBtn")
        self.verticalLayout_3.addWidget(self.savedLocationsIconBtn)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 516, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.settingsIconBtn = QtWidgets.QPushButton(parent=self.sideBarIconWidget)
        self.settingsIconBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/settings_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settingsIconBtn.setIcon(icon6)
        self.settingsIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.settingsIconBtn.setCheckable(True)
        self.settingsIconBtn.setAutoExclusive(True)
        self.settingsIconBtn.setObjectName("settingsIconBtn")
        self.verticalLayout_4.addWidget(self.settingsIconBtn)
        self.gridLayout.addWidget(self.sideBarIconWidget, 0, 0, 1, 1)
        self.sideBarBtnWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.sideBarBtnWidget.setObjectName("sideBarBtnWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sideBarBtnWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.homePageBtn = QtWidgets.QPushButton(parent=self.sideBarBtnWidget)
        self.homePageBtn.setIcon(icon1)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setAutoExclusive(True)
        self.homePageBtn.setObjectName("homePageBtn")
        self.verticalLayout.addWidget(self.homePageBtn)
        self.displayModeBtn = QtWidgets.QPushButton(parent=self.sideBarBtnWidget)
        self.displayModeBtn.setIcon(icon2)
        self.displayModeBtn.setCheckable(True)
        self.displayModeBtn.setAutoExclusive(True)
        self.displayModeBtn.setObjectName("displayModeBtn")
        self.verticalLayout.addWidget(self.displayModeBtn)
        self.syncWithDeviceBtn = QtWidgets.QPushButton(parent=self.sideBarBtnWidget)
        self.syncWithDeviceBtn.setIcon(icon3)
        self.syncWithDeviceBtn.setCheckable(True)
        self.syncWithDeviceBtn.setAutoExclusive(True)
        self.syncWithDeviceBtn.setObjectName("syncWithDeviceBtn")
        self.verticalLayout.addWidget(self.syncWithDeviceBtn)
        self.searchByAreaBtn = QtWidgets.QPushButton(parent=self.sideBarBtnWidget)
        self.searchByAreaBtn.setIcon(icon4)
        self.searchByAreaBtn.setCheckable(True)
        self.searchByAreaBtn.setAutoExclusive(True)
        self.searchByAreaBtn.setObjectName("searchByAreaBtn")
        self.verticalLayout.addWidget(self.searchByAreaBtn)
        self.savedLocationsBtn = QtWidgets.QPushButton(parent=self.sideBarBtnWidget)
        self.savedLocationsBtn.setIcon(icon5)
        self.savedLocationsBtn.setCheckable(True)
        self.savedLocationsBtn.setAutoExclusive(True)
        self.savedLocationsBtn.setObjectName("savedLocationsBtn")
        self.verticalLayout.addWidget(self.savedLocationsBtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 496, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.settingsBtn = QtWidgets.QPushButton(parent=self.sideBarBtnWidget)
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setAutoExclusive(True)
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_2.addWidget(self.settingsBtn)
        self.gridLayout.addWidget(self.sideBarBtnWidget, 0, 1, 1, 1)
        self.mainPageWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.mainPageWidget.setObjectName("mainPageWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainPageWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.topBarWidget = QtWidgets.QWidget(parent=self.mainPageWidget)
        self.topBarWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.topBarWidget.setObjectName("topBarWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.topBarWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sideBarBtn = QtWidgets.QPushButton(parent=self.topBarWidget)
        self.sideBarBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/sideBar_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sideBarBtn.setIcon(icon7)
        self.sideBarBtn.setCheckable(True)
        self.sideBarBtn.setObjectName("sideBarBtn")
        self.horizontalLayout.addWidget(self.sideBarBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.profileBtn = QtWidgets.QPushButton(parent=self.topBarWidget)
        self.profileBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/profileImage_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.profileBtn.setIcon(icon8)
        self.profileBtn.setObjectName("profileBtn")
        self.horizontalLayout.addWidget(self.profileBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.topBarWidget)
        self.pagesWidget = QtWidgets.QStackedWidget(parent=self.mainPageWidget)
        self.pagesWidget.setEnabled(True)
        self.pagesWidget.setObjectName("pagesWidget")
        self.displayModePage = QtWidgets.QWidget()
        self.displayModePage.setObjectName("displayModePage")
        self.pagesWidget.addWidget(self.displayModePage)
        self.widget_4 = QtWidgets.QWidget()
        self.widget_4.setObjectName("widget_4")
        self.pagesWidget.addWidget(self.widget_4)
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.homePage)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = QtWidgets.QWidget(parent=self.homePage)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(parent=self.homePage)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(parent=self.homePage)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addWidget(self.widget_3)
        self.pagesWidget.addWidget(self.homePage)
        self.savedLocationsPage = QtWidgets.QWidget()
        self.savedLocationsPage.setObjectName("savedLocationsPage")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.savedLocationsPage)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_5 = QtWidgets.QWidget(parent=self.savedLocationsPage)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setAccessibleName("")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.horizontalLayout_9.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(parent=self.savedLocationsPage)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(parent=self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(parent=self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6)
        self.horizontalLayout_9.addWidget(self.widget_6)
        self.pagesWidget.addWidget(self.savedLocationsPage)
        self.syncWithDevicePage = QtWidgets.QWidget()
        self.syncWithDevicePage.setObjectName("syncWithDevicePage")
        self.pagesWidget.addWidget(self.syncWithDevicePage)
        self.searchByAreaPage = QtWidgets.QWidget()
        self.searchByAreaPage.setObjectName("searchByAreaPage")
        self.pagesWidget.addWidget(self.searchByAreaPage)
        self.verticalLayout_5.addWidget(self.pagesWidget)
        self.gridLayout.addWidget(self.mainPageWidget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pagesWidget.setCurrentIndex(3)
        self.sideBarBtn.toggled['bool'].connect(self.sideBarIconWidget.setVisible) # type: ignore
        self.sideBarBtn.toggled['bool'].connect(self.sideBarBtnWidget.setHidden) # type: ignore
        self.homePageIconBtn.toggled['bool'].connect(self.homePageBtn.setChecked) # type: ignore
        self.homePageBtn.toggled['bool'].connect(self.homePageIconBtn.setChecked) # type: ignore
        self.displayModeIconBtn.toggled['bool'].connect(self.displayModeBtn.setChecked) # type: ignore
        self.displayModeBtn.toggled['bool'].connect(self.displayModeIconBtn.setChecked) # type: ignore
        self.syncWithDeviceIconBtn.toggled['bool'].connect(self.syncWithDeviceBtn.setChecked) # type: ignore
        self.syncWithDeviceBtn.toggled['bool'].connect(self.syncWithDeviceIconBtn.setChecked) # type: ignore
        self.searchByAreaIconBtn.toggled['bool'].connect(self.searchByAreaBtn.setChecked) # type: ignore
        self.searchByAreaBtn.toggled['bool'].connect(self.searchByAreaIconBtn.setChecked) # type: ignore
        self.exitBtn.clicked.connect(MainWindow.close) # type: ignore
        self.savedLocationsIconBtn.toggled['bool'].connect(self.savedLocationsBtn.setChecked) # type: ignore
        self.savedLocationsBtn.toggled['bool'].connect(self.savedLocationsIconBtn.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.exitBtn, self.homePageIconBtn)
        MainWindow.setTabOrder(self.homePageIconBtn, self.displayModeIconBtn)
        MainWindow.setTabOrder(self.displayModeIconBtn, self.syncWithDeviceIconBtn)
        MainWindow.setTabOrder(self.syncWithDeviceIconBtn, self.searchByAreaIconBtn)
        MainWindow.setTabOrder(self.searchByAreaIconBtn, self.savedLocationsIconBtn)
        MainWindow.setTabOrder(self.savedLocationsIconBtn, self.settingsIconBtn)
        MainWindow.setTabOrder(self.settingsIconBtn, self.homePageBtn)
        MainWindow.setTabOrder(self.homePageBtn, self.displayModeBtn)
        MainWindow.setTabOrder(self.displayModeBtn, self.syncWithDeviceBtn)
        MainWindow.setTabOrder(self.syncWithDeviceBtn, self.searchByAreaBtn)
        MainWindow.setTabOrder(self.searchByAreaBtn, self.savedLocationsBtn)
        MainWindow.setTabOrder(self.savedLocationsBtn, self.settingsBtn)
        MainWindow.setTabOrder(self.settingsBtn, self.sideBarBtn)
        MainWindow.setTabOrder(self.sideBarBtn, self.profileBtn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homePageBtn.setText(_translate("MainWindow", "Home Page"))
        self.displayModeBtn.setText(_translate("MainWindow", "Display Mode"))
        self.syncWithDeviceBtn.setText(_translate("MainWindow", "Sync With Device"))
        self.searchByAreaBtn.setText(_translate("MainWindow", "Search By Area "))
        self.savedLocationsBtn.setText(_translate("MainWindow", "Saved Locations"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))
        self.pushButton.setText(_translate("MainWindow", "More Data >"))
        self.pushButton_2.setText(_translate("MainWindow", "More Data >"))
        self.pushButton_3.setText(_translate("MainWindow", "More Data >"))
        self.label.setText(_translate("MainWindow", "Temperature"))
        self.label_3.setText(_translate("MainWindow", "55 F"))
        self.label_5.setText(_translate("MainWindow", "Last updated 12:00 am"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.label_4.setText(_translate("MainWindow", "38%"))
        self.label_6.setText(_translate("MainWindow", "Last updated 12:00 am"))