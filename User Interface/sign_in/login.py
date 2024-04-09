import sys
import os
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class MainApp(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(800, 600)
		label = QLabel('Main App', parent=self)
		
class LoginWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Login Window')
		self.widow_width, self.window_height = 600, 200
		self.setFixedSize(self.window_width, seld.window_height)
		
		layout = QGridLayout()
		self.setLayout(layout)
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet('''
		QWidget {
			font-size: 25px;
		}
		QLineEdit {
			height: 200px;
		}
	''')
		