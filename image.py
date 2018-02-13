import sys
import os
from PyQt5.QtCore import *
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
		self.initUI(500, 500, 100)

	#init UI with widget
	def initUI(self, W, H, B):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, W, H)

		#need to set image window and center
		label = QLabel(self)
		pixmap = QPixmap(self.firstImg())
		pixmap = pixmap.scaled(self.imgWindow(B),Qt.KeepAspectRatio)
		label.setPixmap(pixmap)
		self.show()

	def imgWindow(self, B):
		size = QSize(self.width - (2 * B), self.height - (2 * B));
		return size

	#reutuns first image in directory /data 
	def firstImg(self):
		imgs = os.listdir(os.path.join('.', 'data'))
		return os.path.join('.', 'data', imgs[0])


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())








