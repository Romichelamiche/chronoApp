import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() #parent init

        self.setWindowTitle("My Amazing Chrono")

        #buttons
        self.button_start = QtWidgets.QPushButton("Start") #Start the chrono
        self.button_stop = QtWidgets.QPushButton("Stop") #Stop the chrono
        self.button_rest = QtWidgets.QPushButton("Reset") #Reset the chrono

        # timer
        self.timer = QtWidgets.QLCDNumber()

        #layout
        self.GridLayout = QtWidgets.QGridLayout()

        self.GridLayout.addWidget(self.button_start, 3, 1)
        self.GridLayout.addWidget(self.button_stop, 3, 2)
        self.GridLayout.addWidget(self.button_rest, 3, 3)
        self.GridLayout.addWidget(self.timer, 1, 1,1,3)



        self.setLayout(self.GridLayout) #installing the gridlayout on the window

#Execute App
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    chrono = MyMainWindow()
    chrono.resize(400, 200)
    chrono.show()

    sys.exit(app.exec_())