# Form implementation generated from reading ui file 'c:\Users\Public\Documents\GitHub\Project---UI-Communications\User Interface\WeatherApp.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 818)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.sideBarBtnWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.sideBarBtnWidget_2.setObjectName("sideBarBtnWidget_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.sideBarBtnWidget_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 28, 24))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/sideBar_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.sideBarBtnWidget_2, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 1, 2, 1)
        self.topBarWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.topBarWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.topBarWidget.setObjectName("topBarWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.topBarWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.profileBtn = QtWidgets.QPushButton(parent=self.topBarWidget)
        self.profileBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/profileImage_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.profileBtn.setIcon(icon1)
        self.profileBtn.setObjectName("profileBtn")
        self.horizontalLayout.addWidget(self.profileBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.topBarWidget, 0, 2, 1, 1)
        self.sideBarWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.sideBarWidget.setObjectName("sideBarWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.sideBarWidget)
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_8 = QtWidgets.QWidget(parent=self.sideBarWidget)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.homePageIconBtn = QtWidgets.QPushButton(parent=self.widget_8)
        self.homePageIconBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/homePage_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homePageIconBtn.setIcon(icon2)
        self.homePageIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.homePageIconBtn.setCheckable(True)
        self.homePageIconBtn.setAutoExclusive(True)
        self.homePageIconBtn.setObjectName("homePageIconBtn")
        self.verticalLayout.addWidget(self.homePageIconBtn)
        self.displayModeIconBtn = QtWidgets.QPushButton(parent=self.widget_8)
        self.displayModeIconBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/displayMode_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.displayModeIconBtn.setIcon(icon3)
        self.displayModeIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.displayModeIconBtn.setCheckable(True)
        self.displayModeIconBtn.setAutoExclusive(True)
        self.displayModeIconBtn.setObjectName("displayModeIconBtn")
        self.verticalLayout.addWidget(self.displayModeIconBtn)
        self.syncWithDeviceIconBtn = QtWidgets.QPushButton(parent=self.widget_8)
        self.syncWithDeviceIconBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/syncWithDevice_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.syncWithDeviceIconBtn.setIcon(icon4)
        self.syncWithDeviceIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.syncWithDeviceIconBtn.setCheckable(True)
        self.syncWithDeviceIconBtn.setAutoExclusive(True)
        self.syncWithDeviceIconBtn.setObjectName("syncWithDeviceIconBtn")
        self.verticalLayout.addWidget(self.syncWithDeviceIconBtn)
        self.searchByAreaIconBtn = QtWidgets.QPushButton(parent=self.widget_8)
        self.searchByAreaIconBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/searchByArea_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.searchByAreaIconBtn.setIcon(icon5)
        self.searchByAreaIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.searchByAreaIconBtn.setCheckable(True)
        self.searchByAreaIconBtn.setAutoExclusive(True)
        self.searchByAreaIconBtn.setObjectName("searchByAreaIconBtn")
        self.verticalLayout.addWidget(self.searchByAreaIconBtn)
        self.savedLocationsIconBtn = QtWidgets.QPushButton(parent=self.widget_8)
        self.savedLocationsIconBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/location_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.savedLocationsIconBtn.setIcon(icon6)
        self.savedLocationsIconBtn.setIconSize(QtCore.QSize(20, 20))
        self.savedLocationsIconBtn.setCheckable(True)
        self.savedLocationsIconBtn.setAutoExclusive(True)
        self.savedLocationsIconBtn.setObjectName("savedLocationsIconBtn")
        self.verticalLayout.addWidget(self.savedLocationsIconBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 507, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_8)
        self.pushButton_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/settings_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_6.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(parent=self.sideBarWidget)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.homePageBtn = QtWidgets.QPushButton(parent=self.widget_9)
        self.homePageBtn.setIcon(icon2)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setAutoExclusive(True)
        self.homePageBtn.setObjectName("homePageBtn")
        self.verticalLayout_2.addWidget(self.homePageBtn)
        self.displayModeBtn = QtWidgets.QPushButton(parent=self.widget_9)
        self.displayModeBtn.setIcon(icon3)
        self.displayModeBtn.setCheckable(True)
        self.displayModeBtn.setAutoExclusive(True)
        self.displayModeBtn.setObjectName("displayModeBtn")
        self.verticalLayout_2.addWidget(self.displayModeBtn)
        self.syncWithDeviceBtn = QtWidgets.QPushButton(parent=self.widget_9)
        self.syncWithDeviceBtn.setIcon(icon4)
        self.syncWithDeviceBtn.setCheckable(True)
        self.syncWithDeviceBtn.setAutoExclusive(True)
        self.syncWithDeviceBtn.setObjectName("syncWithDeviceBtn")
        self.verticalLayout_2.addWidget(self.syncWithDeviceBtn)
        self.searchByAreaBtn = QtWidgets.QPushButton(parent=self.widget_9)
        self.searchByAreaBtn.setIcon(icon5)
        self.searchByAreaBtn.setCheckable(True)
        self.searchByAreaBtn.setAutoExclusive(True)
        self.searchByAreaBtn.setObjectName("searchByAreaBtn")
        self.verticalLayout_2.addWidget(self.searchByAreaBtn)
        self.savedLocationsBtn = QtWidgets.QPushButton(parent=self.widget_9)
        self.savedLocationsBtn.setIcon(icon6)
        self.savedLocationsBtn.setCheckable(True)
        self.savedLocationsBtn.setAutoExclusive(True)
        self.savedLocationsBtn.setObjectName("savedLocationsBtn")
        self.verticalLayout_2.addWidget(self.savedLocationsBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 531, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.settingsBtn = QtWidgets.QPushButton(parent=self.widget_9)
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setAutoExclusive(True)
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_2.addWidget(self.settingsBtn)
        self.horizontalLayout_6.addWidget(self.widget_9)
        self.gridLayout.addWidget(self.sideBarWidget, 1, 0, 1, 1)
        self.mainPageWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.mainPageWidget.setObjectName("mainPageWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainPageWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
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
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_9.addItem(spacerItem3)
        self.tempWidget = QtWidgets.QWidget(parent=self.homePage)
        self.tempWidget.setObjectName("tempWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tempWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tempHLayout = QtWidgets.QHBoxLayout()
        self.tempHLayout.setObjectName("tempHLayout")
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.tempHLayout.addItem(spacerItem4)
        self.tempVLayout = QtWidgets.QVBoxLayout()
        self.tempVLayout.setObjectName("tempVLayout")
        self.tempLinkButton = LinkButton(parent=self.tempWidget)
        self.tempLinkButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tempLinkButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/WeatherIcons/01d.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tempLinkButton.setIcon(icon8)
        self.tempLinkButton.setObjectName("tempLinkButton")
        self.tempVLayout.addWidget(self.tempLinkButton)
        self.line = QtWidgets.QFrame(parent=self.tempWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.tempVLayout.addWidget(self.line)
        self.tempHLayout.addLayout(self.tempVLayout)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.tempHLayout.addItem(spacerItem5)
        self.horizontalLayout_4.addLayout(self.tempHLayout)
        self.verticalLayout_9.addWidget(self.tempWidget)
        self.HumidityWidget = QtWidgets.QWidget(parent=self.homePage)
        self.HumidityWidget.setObjectName("HumidityWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.HumidityWidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.humidityHLayout = QtWidgets.QHBoxLayout()
        self.humidityHLayout.setObjectName("humidityHLayout")
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.humidityHLayout.addItem(spacerItem6)
        self.humidityVLayout = QtWidgets.QVBoxLayout()
        self.humidityVLayout.setObjectName("humidityVLayout")
        self.humidityLinkButton = LinkButton(parent=self.HumidityWidget)
        self.humidityLinkButton.setMaximumSize(QtCore.QSize(16777215, 40))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/WeatherIcons/2682807_drop_high_humidity_percentage_precipitation_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.humidityLinkButton.setIcon(icon9)
        self.humidityLinkButton.setObjectName("humidityLinkButton")
        self.humidityVLayout.addWidget(self.humidityLinkButton)
        self.humdityLine = QtWidgets.QFrame(parent=self.HumidityWidget)
        self.humdityLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.humdityLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.humdityLine.setObjectName("humdityLine")
        self.humidityVLayout.addWidget(self.humdityLine)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        self.humidityVLayout.addItem(spacerItem7)
        self.humidityHLayout.addLayout(self.humidityVLayout)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.humidityHLayout.addItem(spacerItem8)
        self.horizontalLayout_7.addLayout(self.humidityHLayout)
        self.verticalLayout_9.addWidget(self.HumidityWidget)
        self.widget_3 = QtWidgets.QWidget(parent=self.homePage)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(parent=self.widget_3)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout_6.addWidget(self.commandLinkButton_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addWidget(self.widget_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_9.addItem(spacerItem10)
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
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.syncWithDevicePage)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_7 = QtWidgets.QLabel(parent=self.syncWithDevicePage)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_12.addWidget(self.label_7)
        self.widget_7 = QtWidgets.QWidget(parent=self.syncWithDevicePage)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.toolButton = QtWidgets.QToolButton(parent=self.widget_7)
        self.toolButton.setBaseSize(QtCore.QSize(0, 0))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_10.addWidget(self.toolButton)
        self.toolButton_2 = QtWidgets.QToolButton(parent=self.widget_7)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_10.addWidget(self.toolButton_2)
        self.toolButton_3 = QtWidgets.QToolButton(parent=self.widget_7)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_10.addWidget(self.toolButton_3)
        self.verticalLayout_12.addWidget(self.widget_7)
        self.pagesWidget.addWidget(self.syncWithDevicePage)
        self.searchByAreaPage = QtWidgets.QWidget()
        self.searchByAreaPage.setObjectName("searchByAreaPage")
        self.pagesWidget.addWidget(self.searchByAreaPage)
        self.verticalLayout_5.addWidget(self.pagesWidget)
        self.gridLayout.addWidget(self.mainPageWidget, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pagesWidget.setCurrentIndex(2)
        self.searchByAreaIconBtn.toggled['bool'].connect(self.searchByAreaBtn.setChecked) # type: ignore
        self.searchByAreaBtn.toggled['bool'].connect(self.searchByAreaIconBtn.setChecked) # type: ignore
        self.displayModeIconBtn.toggled['bool'].connect(self.displayModeBtn.setChecked) # type: ignore
        self.homePageBtn.toggled['bool'].connect(self.homePageIconBtn.setChecked) # type: ignore
        self.savedLocationsIconBtn.toggled['bool'].connect(self.savedLocationsBtn.setChecked) # type: ignore
        self.syncWithDeviceBtn.toggled['bool'].connect(self.syncWithDeviceIconBtn.setChecked) # type: ignore
        self.savedLocationsBtn.toggled['bool'].connect(self.savedLocationsIconBtn.setChecked) # type: ignore
        self.homePageIconBtn.toggled['bool'].connect(self.homePageBtn.setChecked) # type: ignore
        self.syncWithDeviceIconBtn.toggled['bool'].connect(self.syncWithDeviceBtn.setChecked) # type: ignore
        self.displayModeBtn.toggled['bool'].connect(self.displayModeIconBtn.setChecked) # type: ignore
        self.pushButton.toggled['bool'].connect(self.widget_8.setVisible) # type: ignore
        self.pushButton.toggled['bool'].connect(self.widget_9.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.homePageIconBtn, self.displayModeIconBtn)
        MainWindow.setTabOrder(self.displayModeIconBtn, self.syncWithDeviceIconBtn)
        MainWindow.setTabOrder(self.syncWithDeviceIconBtn, self.searchByAreaIconBtn)
        MainWindow.setTabOrder(self.searchByAreaIconBtn, self.savedLocationsIconBtn)
        MainWindow.setTabOrder(self.savedLocationsIconBtn, self.homePageBtn)
        MainWindow.setTabOrder(self.homePageBtn, self.displayModeBtn)
        MainWindow.setTabOrder(self.displayModeBtn, self.syncWithDeviceBtn)
        MainWindow.setTabOrder(self.syncWithDeviceBtn, self.searchByAreaBtn)
        MainWindow.setTabOrder(self.searchByAreaBtn, self.savedLocationsBtn)
        MainWindow.setTabOrder(self.savedLocationsBtn, self.settingsBtn)
        MainWindow.setTabOrder(self.settingsBtn, self.profileBtn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WeatherApp"))
        self.homePageBtn.setText(_translate("MainWindow", "Home Page"))
        self.displayModeBtn.setText(_translate("MainWindow", "Display Mode"))
        self.syncWithDeviceBtn.setText(_translate("MainWindow", "Sync With Device"))
        self.searchByAreaBtn.setText(_translate("MainWindow", "Search By Area "))
        self.savedLocationsBtn.setText(_translate("MainWindow", "Saved Locations"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))
        self.tempLinkButton.setText(_translate("MainWindow", "Temperture: "))
        self.humidityLinkButton.setText(_translate("MainWindow", "Humidity:"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Add More "))
        self.label.setText(_translate("MainWindow", "Temperature"))
        self.label_3.setText(_translate("MainWindow", "55 F"))
        self.label_5.setText(_translate("MainWindow", "Last updated 12:00 am"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.label_4.setText(_translate("MainWindow", "38%"))
        self.label_6.setText(_translate("MainWindow", "Last updated 12:00 am"))
        self.label_7.setText(_translate("MainWindow", "Paired With Device 12345-abcdefg"))
        self.toolButton.setText(_translate("MainWindow", "Download Data"))
        self.toolButton_2.setText(_translate("MainWindow", "Check Sensors"))
        self.toolButton_3.setText(_translate("MainWindow", "Activate New Sensor"))
from LinkButton import LinkButton
