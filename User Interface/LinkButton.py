import os
from PyQt5 import QtCore, QtGui, QtWidgets


class PushButton(QtWidgets.QCommandLinkButton):
    def __init__(self, *args, **kwargs):
        super(PushButton, self).__init__(*args, **kwargs)
        #self.setStyleSheet('''background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fdfbf7, stop: 1 #6190F2);
        #    border-style: solid;border-width: 2px;
        #    border-radius: 8px;
        #    border-color: #9BB7F0;padding: 3px;''')
        

        icon = self.icon()
        icon_size = self.iconSize()
        # remove icon
        self.setIcon(QtGui.QIcon())
        label_icon = QtWidgets.QLabel()
        label_icon.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        label_icon.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        lay = QtWidgets.QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(label_icon, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        label_icon.setPixmap(icon.pixmap(icon_size))

