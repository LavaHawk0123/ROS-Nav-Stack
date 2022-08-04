#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
import waypoint_probe_deployment

import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty, UInt8
import math
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 232)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.probe = QtWidgets.QPushButton(self.centralwidget)
        self.probe.setGeometry(QtCore.QRect(20, 30, 141, 61))
        self.probe.setObjectName("probe")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.probe.setText(_translate("MainWindow", "Deploy Probe"))
        self.probe.clicked.connect(self.deploy)
        
    def deploy(self):
        # execfile('/home/dishita/ERC-Remote-Navigation-Sim/src/leo_erc_desktop/leo_erc_gazebo/scripts/waypoint_probe_deployment.py')
        # waypoint_probe_deployment.drop_probe()
        os.system('python -m waypoint_probe_deployment')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

