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
        self.extended: bool = False
        self.setStyleSheet("background-color: rgb(0, 160, 220);")

        icon = QtGui.QIcon()
        icon_size = self.iconSize()

        self.label_value = QtWidgets.QLabel()
        self.label_value.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.label_value.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.label_value.setText("0.0 F")
        self.label_value.setFont(QtGui.QFont("Times", 14))

        lay = QtWidgets.QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 10, 0)
        lay.addWidget(self.label_value, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        self.setIcon(QtGui.QIcon())
        self.label_icon = QtWidgets.QLabel()
        self.label_icon.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.label_icon.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        lay.addWidget(self.label_icon, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        self.label_icon.setPixmap(icon.pixmap(icon_size))

#-------------------------------------------------------------------------------------------
    def set_label_text(self, text):
        """Method to set the text of label_value."""
        self.label_value.setText(text)


#-------------------------------------------------------------------------------------------
    def set_arrow_icon(self, icon_path):
        """Method to set the icon of label_icon."""
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon_size = self.iconSize()
        self.label_icon.setPixmap(icon.pixmap(icon_size)) 
    

        

        
        

