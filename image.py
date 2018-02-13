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
		self.width = 250
		self.height = 250
		self.initUI(250, 250, 250)

	#init UI with widget
	def initUI(self, W, H, B):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, W, H)

		label = QLabel(self)
		pixmap = QPixmap(self.firstImg())
		label.setPixmap(pixmap)
		self.show()

	#reutuns first image in directory /data 
	def firstImg(self):
		imgs = os.listdir(os.path.join('.', 'data'))
		return os.path.join('.', 'data', imgs[0])


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())








