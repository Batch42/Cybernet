# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import engine
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from collections import defaultdict as dd
from threading import Thread


class DMWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DMWindow, self).__init__()

        self.setObjectName("PlayerWindow")
        self.resize(1316, 701)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        #Search Window
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 200, 1316, 501))
        self.listWidget.setObjectName("listWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1316, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.searchbox = QtWidgets.QLineEdit(self.frame)
        self.searchbox.setGeometry(QtCore.QRect(self.width()/2-100, 0,150 , 20))
        self.searchbox.setObjectName("searchbox")
        self.searchbox.returnPressed.connect(self.search)
        for p in engine.posts:
            self.listWidget.addItem(p)
            for a in engine.posts[p]:
                self.listWidget.addItem("\t"+a.answer)


        '''self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(1120, 330, 201, 371))
        self.listView.setObjectName("listView")'''
        self.setCentralWidget(self.centralWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.port = 0

        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Cybernet", "Cybernet"))

    def search(self):
        results = engine.search(self.searchbox.text())
        self.listWidget.clear()
        for p in results:
            self.listWidget.addItem(p)
            for a in engine.posts[p]:
                self.listWidget.addItem("\t"+a.answer)


    '''def mouseReleaseEvent(self, QMouseEvent):
        grid=(int(QMouseEvent.pos().x()/self.GRIDSIZE),int(QMouseEvent.pos().y()/self.GRIDSIZE))
        print(grid)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def recv(self,m,name):


    def draw(self,qp):'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    d=DMWindow()
    sys.exit(app.exec_())
