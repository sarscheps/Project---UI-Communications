# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WeatherApp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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

from LinkButton import LinkButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1041, 517)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sideBarBtnWidget_2 = QWidget(self.centralwidget)
        self.sideBarBtnWidget_2.setObjectName(u"sideBarBtnWidget_2")
        self.pushButton = QPushButton(self.sideBarBtnWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 10, 28, 24))
        icon = QIcon()
        icon.addFile(u"icons/BasicIcons/sideBar_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setCheckable(True)

        self.gridLayout.addWidget(self.sideBarBtnWidget_2, 0, 0, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 0, 1, 2, 1)

        self.topBarWidget = QWidget(self.centralwidget)
        self.topBarWidget.setObjectName(u"topBarWidget")
        self.topBarWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.topBarWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.profileBtn = QPushButton(self.topBarWidget)
        self.profileBtn.setObjectName(u"profileBtn")
        icon1 = QIcon()
        icon1.addFile(u"icons/BasicIcons/profileImage_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.profileBtn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.topBarWidget, 0, 2, 1, 1)

        self.sideBarWidget = QWidget(self.centralwidget)
        self.sideBarWidget.setObjectName(u"sideBarWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.sideBarWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.widget_8 = QWidget(self.sideBarWidget)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout = QVBoxLayout(self.widget_8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.homePageIconBtn = QPushButton(self.widget_8)
        self.homePageIconBtn.setObjectName(u"homePageIconBtn")
        icon2 = QIcon()
        icon2.addFile(u"icons/BasicIcons/homePage_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homePageIconBtn.setIcon(icon2)
        self.homePageIconBtn.setIconSize(QSize(20, 20))
        self.homePageIconBtn.setCheckable(True)
        self.homePageIconBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.homePageIconBtn)

        self.displayModeIconBtn = QPushButton(self.widget_8)
        self.displayModeIconBtn.setObjectName(u"displayModeIconBtn")
        icon3 = QIcon()
        icon3.addFile(u"icons/BasicIcons/displayMode_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.displayModeIconBtn.setIcon(icon3)
        self.displayModeIconBtn.setIconSize(QSize(20, 20))
        self.displayModeIconBtn.setCheckable(True)
        self.displayModeIconBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.displayModeIconBtn)

        self.syncWithDeviceIconBtn = QPushButton(self.widget_8)
        self.syncWithDeviceIconBtn.setObjectName(u"syncWithDeviceIconBtn")
        icon4 = QIcon()
        icon4.addFile(u"icons/BasicIcons/syncWithDevice_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.syncWithDeviceIconBtn.setIcon(icon4)
        self.syncWithDeviceIconBtn.setIconSize(QSize(20, 20))
        self.syncWithDeviceIconBtn.setCheckable(True)
        self.syncWithDeviceIconBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.syncWithDeviceIconBtn)

        self.searchByAreaIconBtn = QPushButton(self.widget_8)
        self.searchByAreaIconBtn.setObjectName(u"searchByAreaIconBtn")
        icon5 = QIcon()
        icon5.addFile(u"icons/BasicIcons/searchByArea_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchByAreaIconBtn.setIcon(icon5)
        self.searchByAreaIconBtn.setIconSize(QSize(20, 20))
        self.searchByAreaIconBtn.setCheckable(True)
        self.searchByAreaIconBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.searchByAreaIconBtn)

        self.savedLocationsIconBtn = QPushButton(self.widget_8)
        self.savedLocationsIconBtn.setObjectName(u"savedLocationsIconBtn")
        icon6 = QIcon()
        icon6.addFile(u"icons/BasicIcons/location_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.savedLocationsIconBtn.setIcon(icon6)
        self.savedLocationsIconBtn.setIconSize(QSize(20, 20))
        self.savedLocationsIconBtn.setCheckable(True)
        self.savedLocationsIconBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.savedLocationsIconBtn)

        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_2 = QPushButton(self.widget_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon7 = QIcon()
        icon7.addFile(u"icons/BasicIcons/settings_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_6.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.sideBarWidget)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_2 = QVBoxLayout(self.widget_9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.homePageBtn = QPushButton(self.widget_9)
        self.homePageBtn.setObjectName(u"homePageBtn")
        self.homePageBtn.setIcon(icon2)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.homePageBtn)

        self.displayModeBtn = QPushButton(self.widget_9)
        self.displayModeBtn.setObjectName(u"displayModeBtn")
        self.displayModeBtn.setIcon(icon3)
        self.displayModeBtn.setCheckable(True)
        self.displayModeBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.displayModeBtn)

        self.syncWithDeviceBtn = QPushButton(self.widget_9)
        self.syncWithDeviceBtn.setObjectName(u"syncWithDeviceBtn")
        self.syncWithDeviceBtn.setIcon(icon4)
        self.syncWithDeviceBtn.setCheckable(True)
        self.syncWithDeviceBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.syncWithDeviceBtn)

        self.searchByAreaBtn = QPushButton(self.widget_9)
        self.searchByAreaBtn.setObjectName(u"searchByAreaBtn")
        self.searchByAreaBtn.setIcon(icon5)
        self.searchByAreaBtn.setCheckable(True)
        self.searchByAreaBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.searchByAreaBtn)

        self.savedLocationsBtn = QPushButton(self.widget_9)
        self.savedLocationsBtn.setObjectName(u"savedLocationsBtn")
        self.savedLocationsBtn.setIcon(icon6)
        self.savedLocationsBtn.setCheckable(True)
        self.savedLocationsBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.savedLocationsBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 531, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.settingsBtn = QPushButton(self.widget_9)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settingsBtn)


        self.horizontalLayout_6.addWidget(self.widget_9)


        self.gridLayout.addWidget(self.sideBarWidget, 1, 0, 1, 1)

        self.mainPageWidget = QWidget(self.centralwidget)
        self.mainPageWidget.setObjectName(u"mainPageWidget")
        self.verticalLayout_5 = QVBoxLayout(self.mainPageWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
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
        self.homePageTopSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_9.addItem(self.homePageTopSpacer)

        self.tempWidget = QWidget(self.homePage)
        self.tempWidget.setObjectName(u"tempWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.tempWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tempHLayout = QHBoxLayout()
        self.tempHLayout.setObjectName(u"tempHLayout")
        self.tempLeftHSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.tempHLayout.addItem(self.tempLeftHSpacer)

        self.tempVLayout = QVBoxLayout()
        self.tempVLayout.setObjectName(u"tempVLayout")
        self.tempLinkButton = LinkButton(self.tempWidget)
        self.tempLinkButton.setObjectName(u"tempLinkButton")
        self.tempLinkButton.setMaximumSize(QSize(16777210, 40))
        self.tempLinkButton.setLayoutDirection(Qt.LeftToRight)
        icon8 = QIcon()
        icon8.addFile(u"icons/WeatherIcons/01d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tempLinkButton.setIcon(icon8)

        self.tempVLayout.addWidget(self.tempLinkButton)

        self.line = QFrame(self.tempWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.tempVLayout.addWidget(self.line)


        self.tempHLayout.addLayout(self.tempVLayout)

        self.tempRightHSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.tempHLayout.addItem(self.tempRightHSpacer)


        self.horizontalLayout_4.addLayout(self.tempHLayout)


        self.verticalLayout_9.addWidget(self.tempWidget)

        self.HumidityWidget = QWidget(self.homePage)
        self.HumidityWidget.setObjectName(u"HumidityWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.HumidityWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.humidityHLayout = QHBoxLayout()
        self.humidityHLayout.setObjectName(u"humidityHLayout")
        self.humidityHSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.humidityHLayout.addItem(self.humidityHSpacer)

        self.humidityVLayout = QVBoxLayout()
        self.humidityVLayout.setObjectName(u"humidityVLayout")
        self.humidityLinkButton = LinkButton(self.HumidityWidget)
        self.humidityLinkButton.setObjectName(u"humidityLinkButton")
        self.humidityLinkButton.setMaximumSize(QSize(16777215, 40))
        icon9 = QIcon()
        icon9.addFile(u"icons/WeatherIcons/2682807_drop_high_humidity_percentage_precipitation_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.humidityLinkButton.setIcon(icon9)

        self.humidityVLayout.addWidget(self.humidityLinkButton)

        self.humdityLine = QFrame(self.HumidityWidget)
        self.humdityLine.setObjectName(u"humdityLine")
        self.humdityLine.setFrameShape(QFrame.HLine)
        self.humdityLine.setFrameShadow(QFrame.Sunken)

        self.humidityVLayout.addWidget(self.humdityLine)


        self.humidityHLayout.addLayout(self.humidityVLayout)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.humidityHLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_7.addLayout(self.humidityHLayout)


        self.verticalLayout_9.addWidget(self.HumidityWidget)

        self.addMoreWidget = QWidget(self.homePage)
        self.addMoreWidget.setObjectName(u"addMoreWidget")
        self.horizontalLayout_8 = QHBoxLayout(self.addMoreWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.addMoreHLayout = QHBoxLayout()
        self.addMoreHLayout.setObjectName(u"addMoreHLayout")
        self.addMoreLeftSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.addMoreHLayout.addItem(self.addMoreLeftSpacer)

        self.addMoreVLayout = QVBoxLayout()
        self.addMoreVLayout.setObjectName(u"addMoreVLayout")
        self.addMoreLinkButton = QCommandLinkButton(self.addMoreWidget)
        self.addMoreLinkButton.setObjectName(u"addMoreLinkButton")
        self.addMoreLinkButton.setMaximumSize(QSize(16777215, 40))
        icon10 = QIcon()
        icon10.addFile(u"icons/BasicIcons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addMoreLinkButton.setIcon(icon10)

        self.addMoreVLayout.addWidget(self.addMoreLinkButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.addMoreVLayout.addItem(self.verticalSpacer_3)


        self.addMoreHLayout.addLayout(self.addMoreVLayout)

        self.addMoreRightSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.addMoreHLayout.addItem(self.addMoreRightSpacer)


        self.horizontalLayout_8.addLayout(self.addMoreHLayout)


        self.verticalLayout_9.addWidget(self.addMoreWidget)

        self.homePageButtomSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.homePageButtomSpacer)

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
        font = QFont()
        font.setPointSize(28)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(False)
        self.label_3.setFont(font1)
#if QT_CONFIG(accessibility)
        self.label_3.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)


        self.horizontalLayout_9.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.savedLocationsPage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_11 = QVBoxLayout(self.widget_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_2)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(40)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_4)

        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
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


        self.gridLayout.addWidget(self.mainPageWidget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.homePageIconBtn, self.displayModeIconBtn)
        QWidget.setTabOrder(self.displayModeIconBtn, self.syncWithDeviceIconBtn)
        QWidget.setTabOrder(self.syncWithDeviceIconBtn, self.searchByAreaIconBtn)
        QWidget.setTabOrder(self.searchByAreaIconBtn, self.savedLocationsIconBtn)
        QWidget.setTabOrder(self.savedLocationsIconBtn, self.homePageBtn)
        QWidget.setTabOrder(self.homePageBtn, self.displayModeBtn)
        QWidget.setTabOrder(self.displayModeBtn, self.syncWithDeviceBtn)
        QWidget.setTabOrder(self.syncWithDeviceBtn, self.searchByAreaBtn)
        QWidget.setTabOrder(self.searchByAreaBtn, self.savedLocationsBtn)
        QWidget.setTabOrder(self.savedLocationsBtn, self.settingsBtn)
        QWidget.setTabOrder(self.settingsBtn, self.profileBtn)

        self.retranslateUi(MainWindow)
        self.searchByAreaIconBtn.toggled.connect(self.searchByAreaBtn.setChecked)
        self.searchByAreaBtn.toggled.connect(self.searchByAreaIconBtn.setChecked)
        self.displayModeIconBtn.toggled.connect(self.displayModeBtn.setChecked)
        self.homePageBtn.toggled.connect(self.homePageIconBtn.setChecked)
        self.savedLocationsIconBtn.toggled.connect(self.savedLocationsBtn.setChecked)
        self.syncWithDeviceBtn.toggled.connect(self.syncWithDeviceIconBtn.setChecked)
        self.savedLocationsBtn.toggled.connect(self.savedLocationsIconBtn.setChecked)
        self.homePageIconBtn.toggled.connect(self.homePageBtn.setChecked)
        self.syncWithDeviceIconBtn.toggled.connect(self.syncWithDeviceBtn.setChecked)
        self.displayModeBtn.toggled.connect(self.displayModeIconBtn.setChecked)
        self.pushButton.toggled.connect(self.widget_8.setVisible)
        self.pushButton.toggled.connect(self.widget_9.setHidden)

        self.pagesWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WeatherApp", None))
        self.pushButton.setText("")
        self.profileBtn.setText("")
        self.homePageIconBtn.setText("")
        self.displayModeIconBtn.setText("")
        self.syncWithDeviceIconBtn.setText("")
        self.searchByAreaIconBtn.setText("")
        self.savedLocationsIconBtn.setText("")
        self.pushButton_2.setText("")
        self.homePageBtn.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.displayModeBtn.setText(QCoreApplication.translate("MainWindow", u"Display Mode", None))
        self.syncWithDeviceBtn.setText(QCoreApplication.translate("MainWindow", u"Sync With Device", None))
        self.searchByAreaBtn.setText(QCoreApplication.translate("MainWindow", u"Search By Area ", None))
        self.savedLocationsBtn.setText(QCoreApplication.translate("MainWindow", u"Saved Locations", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tempLinkButton.setText(QCoreApplication.translate("MainWindow", u"Temperture: ", None))
        self.humidityLinkButton.setText(QCoreApplication.translate("MainWindow", u"Humidity:", None))
        self.addMoreLinkButton.setText(QCoreApplication.translate("MainWindow", u"Add More ", None))
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

