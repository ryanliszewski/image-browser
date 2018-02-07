import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
	
	#init window
	def __init__(self):
		super().__init__()
		self.title = 'Image Browser'
		self.left = 100 
		self.top = 100
		self.width = 0
		self.height = 0
		self.directories = []
		self.initUI()

	#init UI with widget
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		label = QLabel(self)
		pixmap = QPixmap('./data/Jacka.png')
		label.setPixmap(pixmap)
		self.show()

	def directory(self):
		self.directories = os.listdir(os.path.join('.', 'data'))
		print(self.directories)

	def configure(w, h, b):


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())








