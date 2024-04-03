import os
from PyQt6 import QtCore, QtGui, QtWidgets


class LinkButton(QtWidgets.QCommandLinkButton):
    def __init__(self, *args, **kwargs):
        super(LinkButton, self).__init__(*args, **kwargs)
        #self.setStyleSheet('''background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fdfbf7, stop: 1 #6190F2);
        #    border-style: solid;border-width: 2px;
        #    border-radius: 8px;
        #    border-color: #9BB7F0;padding: 3px;''')
        
        # remove icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Public\\Documents\\GitHub\\Project---UI-Communications\\User Interface\\icons/BasicIcons/MoreArrIcon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon_size = self.iconSize()

        self.setIcon(QtGui.QIcon())
        label_icon = QtWidgets.QLabel()
        label_icon.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        label_icon.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        lay = QtWidgets.QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 10, 0)
        lay.addWidget(label_icon, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        label_icon.setPixmap(icon.pixmap(icon_size))

