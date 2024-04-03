# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WeatherAppRFJmLe.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

from linkbutton import LinkButton
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 316)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sideBarIconWidget = QWidget(self.centralwidget)
        self.sideBarIconWidget.setObjectName(u"sideBarIconWidget")
        self.verticalLayout_4 = QVBoxLayout(self.sideBarIconWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.exitBtn = QPushButton(self.sideBarIconWidget)
        self.exitBtn.setObjectName(u"exitBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/exit_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon)
        self.exitBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.exitBtn)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.homePageIconBtn = QPushButton(self.sideBarIconWidget)
        self.homePageIconBtn.setObjectName(u"homePageIconBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/homePage_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homePageIconBtn.setIcon(icon1)
        self.homePageIconBtn.setIconSize(QSize(20, 20))
        self.homePageIconBtn.setCheckable(True)
        self.homePageIconBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.homePageIconBtn)

        self.displayModeIconBtn = QPushButton(self.sideBarIconWidget)
        self.displayModeIconBtn.setObjectName(u"displayModeIconBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/displayMode_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.displayModeIconBtn.setIcon(icon2)
        self.displayModeIconBtn.setIconSize(QSize(20, 20))
        self.displayModeIconBtn.setCheckable(True)
        self.displayModeIconBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.displayModeIconBtn)

        self.syncWithDeviceIconBtn = QPushButton(self.sideBarIconWidget)
        self.syncWithDeviceIconBtn.setObjectName(u"syncWithDeviceIconBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/syncWithDevice_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.syncWithDeviceIconBtn.setIcon(icon3)
        self.syncWithDeviceIconBtn.setIconSize(QSize(20, 20))
        self.syncWithDeviceIconBtn.setCheckable(True)
        self.syncWithDeviceIconBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.syncWithDeviceIconBtn)

        self.searchByAreaIconBtn = QPushButton(self.sideBarIconWidget)
        self.searchByAreaIconBtn.setObjectName(u"searchByAreaIconBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/searchByArea_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchByAreaIconBtn.setIcon(icon4)
        self.searchByAreaIconBtn.setIconSize(QSize(20, 20))
        self.searchByAreaIconBtn.setCheckable(True)
        self.searchByAreaIconBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.searchByAreaIconBtn)

        self.savedLocationsIconBtn = QPushButton(self.sideBarIconWidget)
        self.savedLocationsIconBtn.setObjectName(u"savedLocationsIconBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/savedLocations_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.savedLocationsIconBtn.setIcon(icon5)
        self.savedLocationsIconBtn.setIconSize(QSize(20, 20))
        self.savedLocationsIconBtn.setCheckable(True)
        self.savedLocationsIconBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.savedLocationsIconBtn)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 516, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.settingsIconBtn = QPushButton(self.sideBarIconWidget)
        self.settingsIconBtn.setObjectName(u"settingsIconBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/settings_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsIconBtn.setIcon(icon6)
        self.settingsIconBtn.setIconSize(QSize(20, 20))
        self.settingsIconBtn.setCheckable(True)
        self.settingsIconBtn.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.settingsIconBtn)


        self.gridLayout.addWidget(self.sideBarIconWidget, 0, 0, 1, 1)

        self.sideBarBtnWidget = QWidget(self.centralwidget)
        self.sideBarBtnWidget.setObjectName(u"sideBarBtnWidget")
        self.verticalLayout_2 = QVBoxLayout(self.sideBarBtnWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homePageBtn = QPushButton(self.sideBarBtnWidget)
        self.homePageBtn.setObjectName(u"homePageBtn")
        icon7 = QIcon()
        icon7.addFile(u"icons/Basic Icons/homePage_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homePageBtn.setIcon(icon7)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.homePageBtn)

        self.displayModeBtn = QPushButton(self.sideBarBtnWidget)
        self.displayModeBtn.setObjectName(u"displayModeBtn")
        self.displayModeBtn.setIcon(icon2)
        self.displayModeBtn.setCheckable(True)
        self.displayModeBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.displayModeBtn)

        self.syncWithDeviceBtn = QPushButton(self.sideBarBtnWidget)
        self.syncWithDeviceBtn.setObjectName(u"syncWithDeviceBtn")
        self.syncWithDeviceBtn.setIcon(icon3)
        self.syncWithDeviceBtn.setCheckable(True)
        self.syncWithDeviceBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.syncWithDeviceBtn)

        self.searchByAreaBtn = QPushButton(self.sideBarBtnWidget)
        self.searchByAreaBtn.setObjectName(u"searchByAreaBtn")
        self.searchByAreaBtn.setIcon(icon4)
        self.searchByAreaBtn.setCheckable(True)
        self.searchByAreaBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.searchByAreaBtn)

        self.savedLocationsBtn = QPushButton(self.sideBarBtnWidget)
        self.savedLocationsBtn.setObjectName(u"savedLocationsBtn")
        self.savedLocationsBtn.setIcon(icon5)
        self.savedLocationsBtn.setCheckable(True)
        self.savedLocationsBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.savedLocationsBtn)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 496, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.settingsBtn = QPushButton(self.sideBarBtnWidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settingsBtn)


        self.gridLayout.addWidget(self.sideBarBtnWidget, 0, 1, 1, 1)

        self.mainPageWidget = QWidget(self.centralwidget)
        self.mainPageWidget.setObjectName(u"mainPageWidget")
        self.verticalLayout_5 = QVBoxLayout(self.mainPageWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.topBarWidget = QWidget(self.mainPageWidget)
        self.topBarWidget.setObjectName(u"topBarWidget")
        self.topBarWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.topBarWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sideBarBtn = QPushButton(self.topBarWidget)
        self.sideBarBtn.setObjectName(u"sideBarBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/sideBar_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sideBarBtn.setIcon(icon8)
        self.sideBarBtn.setCheckable(True)

        self.horizontalLayout.addWidget(self.sideBarBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.profileBtn = QPushButton(self.topBarWidget)
        self.profileBtn.setObjectName(u"profileBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/profileImage_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon9)

        self.horizontalLayout.addWidget(self.profileBtn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.topBarWidget)

        self.pagesWidget = QStackedWidget(self.mainPageWidget)
        self.pagesWidget.setObjectName(u"pagesWidget")
        self.pagesWidget.setEnabled(True)
        self.displayModePage = QWidget()
        self.displayModePage.setObjectName(u"displayModePage")
        self.pagesWidget.addWidget(self.displayModePage)
        self.widget_4 = QWidget()
        self.widget_4.setObjectName(u"widget_4")
        self.pagesWidget.addWidget(self.widget_4)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_9 = QVBoxLayout(self.homePage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tempWidget = QWidget(self.homePage)
        self.tempWidget.setObjectName(u"tempWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.tempWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tempHLayout = QHBoxLayout()
        self.tempHLayout.setObjectName(u"tempHLayout")
        self.tempLeftHSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.tempHLayout.addItem(self.tempLeftHSpacer)

        self.tempVLayout = QVBoxLayout()
        self.tempVLayout.setObjectName(u"tempVLayout")
        self.tempButtomVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tempVLayout.addItem(self.tempButtomVSpacer)

        self.tempLinkButton = LinkButton(self.tempWidget)
        self.tempLinkButton.setObjectName(u"tempLinkButton")
        self.tempLinkButton.setMaximumSize(QSize(16777215, 60))
        self.tempLinkButton.setLayoutDirection(Qt.LeftToRight)
        icon10 = QIcon()
        icon10.addFile(u"icons/Weather Icons/01d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tempLinkButton.setIcon(icon10)

        self.tempVLayout.addWidget(self.tempLinkButton)

        self.line = QFrame(self.tempWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.tempVLayout.addWidget(self.line)

        self.tempTopVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tempVLayout.addItem(self.tempTopVSpacer)


        self.tempHLayout.addLayout(self.tempVLayout)

        self.tempRightHSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.tempHLayout.addItem(self.tempRightHSpacer)


        self.horizontalLayout_4.addLayout(self.tempHLayout)


        self.verticalLayout_9.addWidget(self.tempWidget)

        self.widget_2 = QWidget(self.homePage)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font = QFont()
        font.setBold(True)
        self.pushButton_2.setFont(font)

        self.verticalLayout_7.addWidget(self.pushButton_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.homePage)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.commandLinkButton_2 = QCommandLinkButton(self.widget_3)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")

        self.verticalLayout_6.addWidget(self.commandLinkButton_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)


        self.verticalLayout_9.addWidget(self.widget_3)

        self.pagesWidget.addWidget(self.homePage)
        self.savedLocationsPage = QWidget()
        self.savedLocationsPage.setObjectName(u"savedLocationsPage")
        self.horizontalLayout_9 = QHBoxLayout(self.savedLocationsPage)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_5 = QWidget(self.savedLocationsPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(28)
        font1.setUnderline(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(40)
        font2.setBold(False)
        self.label_3.setFont(font2)
#if QT_CONFIG(accessibility)
        self.label_3.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(15)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)


        self.horizontalLayout_9.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.savedLocationsPage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_11 = QVBoxLayout(self.widget_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_2)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(40)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_4)

        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)


        self.horizontalLayout_9.addWidget(self.widget_6)

        self.pagesWidget.addWidget(self.savedLocationsPage)
        self.syncWithDevicePage = QWidget()
        self.syncWithDevicePage.setObjectName(u"syncWithDevicePage")
        self.verticalLayout_12 = QVBoxLayout(self.syncWithDevicePage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.syncWithDevicePage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_7)

        self.widget_7 = QWidget(self.syncWithDevicePage)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.widget_7)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setBaseSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.widget_7)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_10.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.widget_7)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_10.addWidget(self.toolButton_3)


        self.verticalLayout_12.addWidget(self.widget_7)

        self.pagesWidget.addWidget(self.syncWithDevicePage)
        self.searchByAreaPage = QWidget()
        self.searchByAreaPage.setObjectName(u"searchByAreaPage")
        self.pagesWidget.addWidget(self.searchByAreaPage)

        self.verticalLayout_5.addWidget(self.pagesWidget)


        self.gridLayout.addWidget(self.mainPageWidget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.exitBtn, self.homePageIconBtn)
        QWidget.setTabOrder(self.homePageIconBtn, self.displayModeIconBtn)
        QWidget.setTabOrder(self.displayModeIconBtn, self.syncWithDeviceIconBtn)
        QWidget.setTabOrder(self.syncWithDeviceIconBtn, self.searchByAreaIconBtn)
        QWidget.setTabOrder(self.searchByAreaIconBtn, self.savedLocationsIconBtn)
        QWidget.setTabOrder(self.savedLocationsIconBtn, self.settingsIconBtn)
        QWidget.setTabOrder(self.settingsIconBtn, self.homePageBtn)
        QWidget.setTabOrder(self.homePageBtn, self.displayModeBtn)
        QWidget.setTabOrder(self.displayModeBtn, self.syncWithDeviceBtn)
        QWidget.setTabOrder(self.syncWithDeviceBtn, self.searchByAreaBtn)
        QWidget.setTabOrder(self.searchByAreaBtn, self.savedLocationsBtn)
        QWidget.setTabOrder(self.savedLocationsBtn, self.settingsBtn)
        QWidget.setTabOrder(self.settingsBtn, self.sideBarBtn)
        QWidget.setTabOrder(self.sideBarBtn, self.profileBtn)

        self.retranslateUi(MainWindow)
        self.sideBarBtn.toggled.connect(self.sideBarIconWidget.setVisible)
        self.sideBarBtn.toggled.connect(self.sideBarBtnWidget.setHidden)
        self.homePageIconBtn.toggled.connect(self.homePageBtn.setChecked)
        self.homePageBtn.toggled.connect(self.homePageIconBtn.setChecked)
        self.displayModeIconBtn.toggled.connect(self.displayModeBtn.setChecked)
        self.displayModeBtn.toggled.connect(self.displayModeIconBtn.setChecked)
        self.syncWithDeviceIconBtn.toggled.connect(self.syncWithDeviceBtn.setChecked)
        self.syncWithDeviceBtn.toggled.connect(self.syncWithDeviceIconBtn.setChecked)
        self.searchByAreaIconBtn.toggled.connect(self.searchByAreaBtn.setChecked)
        self.searchByAreaBtn.toggled.connect(self.searchByAreaIconBtn.setChecked)
        self.exitBtn.clicked.connect(MainWindow.close)
        self.savedLocationsIconBtn.toggled.connect(self.savedLocationsBtn.setChecked)
        self.savedLocationsBtn.toggled.connect(self.savedLocationsIconBtn.setChecked)

        self.pagesWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WeatherApp", None))
        self.exitBtn.setText("")
        self.homePageIconBtn.setText("")
        self.displayModeIconBtn.setText("")
        self.syncWithDeviceIconBtn.setText("")
        self.searchByAreaIconBtn.setText("")
        self.savedLocationsIconBtn.setText("")
        self.settingsIconBtn.setText("")
        self.homePageBtn.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.displayModeBtn.setText(QCoreApplication.translate("MainWindow", u"Display Mode", None))
        self.syncWithDeviceBtn.setText(QCoreApplication.translate("MainWindow", u"Sync With Device", None))
        self.searchByAreaBtn.setText(QCoreApplication.translate("MainWindow", u"Search By Area ", None))
        self.savedLocationsBtn.setText(QCoreApplication.translate("MainWindow", u"Saved Locations", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.sideBarBtn.setText("")
        self.profileBtn.setText("")
        self.tempLinkButton.setText(QCoreApplication.translate("MainWindow", u"Temperture: ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"More Data >", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"55 F", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Last updated 12:00 am", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"38%", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Last updated 12:00 am", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Paired With Device 12345-abcdefg", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Download Data", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Check Sensors", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"Activate New Sensor", None))
    # retranslateUi

