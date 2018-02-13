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
		self.initUI(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

	#init UI with widget
	def initUI(self, W, H, B):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, W, H)

		self.label = QLabel(self)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setStyleSheet("border: " + str(B) + " solid black")

		self.pixmap = QPixmap(self.firstImg())
		self.pixmap = self.pixmap.scaled(self.imgSize(B, W) , self.imgSize(B, H), Qt.KeepAspectRatio)
		self.label.setPixmap(self.pixmap)

		self.layout = QHBoxLayout()
		self.layout.addWidget(self.label)

		self.setLayout(self.layout)
		self.show()
		
	#returns image size
	def imgSize(self, B, X):
		size = X - (2 * B)
		return size

	#reutuns first image in directory /data 
	def firstImg(self):
		imgs = os.listdir(os.path.join('.', 'data'))
		print(imgs)
		return os.path.join('.', 'data', imgs[0])


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())








