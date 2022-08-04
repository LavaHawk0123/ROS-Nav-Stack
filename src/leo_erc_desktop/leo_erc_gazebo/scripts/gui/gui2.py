#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
# import waypoint_probe_deployment
import os 
import rospy
from std_msgs.msg import Empty, UInt8

class Ui_Navigation_Task(object):
    def setupUi(self, Navigation_Task):
        
        # rospy.Subscriber("/probe_deployment_unit/probes_dropped", UInt8, self.probe_callback)
        self.counter_probe = 0
        Navigation_Task.setObjectName("Navigation_Task")
        Navigation_Task.resize(615, 417)
        self.centralwidget = QtWidgets.QWidget(Navigation_Task)
        self.centralwidget.setObjectName("centralwidget")
        self.probe = QtWidgets.QPushButton(self.centralwidget)
        self.probe.setGeometry(QtCore.QRect(20, 60, 141, 61))
        self.probe.setFlat(False)
        self.probe.setObjectName("probe")
        self.counter = QtWidgets.QLabel(self.centralwidget)
        self.counter.setGeometry(QtCore.QRect(80, 10, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(33)
        self.counter.setFont(font)
        self.counter.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.counter.setStyleSheet("")
        self.counter.setObjectName("counter")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(170, 0, 20, 141))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 130, 181, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        Navigation_Task.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Navigation_Task)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        Navigation_Task.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Navigation_Task)
        self.statusbar.setObjectName("statusbar")
        Navigation_Task.setStatusBar(self.statusbar)

        self.retranslateUi(Navigation_Task)
        QtCore.QMetaObject.connectSlotsByName(Navigation_Task)

    def retranslateUi(self, Navigation_Task):
        _translate = QtCore.QCoreApplication.translate
        Navigation_Task.setWindowTitle(_translate("Navigation_Task", "MainWindow"))
        self.probe.setText(_translate("Navigation_Task", "Deploy Probe"))
        self.probe.clicked.connect(self.deploy)
        self.counter.setText(_translate("Navigation_Task", "0"))
        
    def deploy(self):
        self.counter_probe += 1
        os.system('rosrun leo_erc_gazebo waypoint_probe_deployment.py')
        if self.counter_probe <= 5:
            self.counter.setText(str(self.counter_probe))
            
    # def probe_callback(self, msg):
    #     self.counter_probe = msg.data   
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Navigation_Task = QtWidgets.QMainWindow()
    ui = Ui_Navigation_Task()
    ui.setupUi(Navigation_Task)
    Navigation_Task.show()
    sys.exit(app.exec_())

