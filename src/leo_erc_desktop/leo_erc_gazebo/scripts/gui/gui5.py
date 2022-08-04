#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal
import os 
import rospy
from std_msgs.msg import Empty, UInt8
import numpy as np
import actionlib

class Ui_Navigation_Task(object):
    def __init__(self):
        self.goals = np.array([[0,0],[2.39,-1.549,0.000,0.000,0.000,0.377,0.926],[0,1],[5,6],[7,8],[9,10]]) #Goals given by ERC
        self.goals_erc = rospy.get_param("/goals")
        print(self.goals_erc)
        self.nav_goal = MoveBaseGoal()
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        
    def setupUi(self, Navigation_Task):
        self.goalno = ""
        self.counter_probe = 0
        Navigation_Task.setObjectName("Navigation_Task")
        Navigation_Task.resize(441, 521)
        
        self.centralwidget = QtWidgets.QWidget(Navigation_Task)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 130, 181, 261))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        # capture centre
        self.capture = QtWidgets.QPushButton(self.frame_2)
        self.capture.setGeometry(QtCore.QRect(50, 50, 81, 51))
        self.capture.setObjectName("capture")
        
        # capture left
        self.capture_left = QtWidgets.QPushButton(self.frame_2)
        self.capture_left.setGeometry(QtCore.QRect(20, 120, 141, 51))
        self.capture_left.setObjectName("capture_left")
        
        # capture right
        self.capture_right = QtWidgets.QPushButton(self.frame_2)
        self.capture_right.setGeometry(QtCore.QRect(20, 190, 141, 51))
        self.capture_right.setObjectName("capture_right")
        
        # taking images label
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # frame 1
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 181, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        # probe button
        self.probe = QtWidgets.QPushButton(self.frame)
        self.probe.setGeometry(QtCore.QRect(20, 60, 141, 61))
        self.probe.setFlat(False)
        self.probe.setObjectName("probe")
        
        # probe counter
        self.counter = QtWidgets.QLabel(self.frame)
        self.counter.setGeometry(QtCore.QRect(80, 10, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(33)
        self.counter.setFont(font)
        self.counter.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.counter.setStyleSheet("")
        self.counter.setObjectName("counter")
        
        # frame 3
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(180, 0, 261, 391))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        # m_b goal label
        self.mlabel = QtWidgets.QLabel(self.frame_3)
        self.mlabel.setGeometry(QtCore.QRect(20, 10, 231, 20))
        self.mlabel.setObjectName("mlabel")
        
        #Goal 1 - move base
        self.Goal1 = QtWidgets.QPushButton(self.frame_3)
        self.Goal1.setGeometry(QtCore.QRect(90, 50, 89, 25))
        self.Goal1.setObjectName("Goal1")
        
        #Goal 2 - move base
        self.Goal2 = QtWidgets.QPushButton(self.frame_3)
        self.Goal2.setGeometry(QtCore.QRect(90, 100, 89, 25))
        self.Goal2.setObjectName("Goal2")
        
        #Goal 3 - move base
        self.Goal3 = QtWidgets.QPushButton(self.frame_3)
        self.Goal3.setGeometry(QtCore.QRect(90, 150, 89, 25))
        self.Goal3.setObjectName("Goal3")
        
        #Goal 4 - move base
        self.Goal4 = QtWidgets.QPushButton(self.frame_3)
        self.Goal4.setGeometry(QtCore.QRect(90, 200, 89, 25))
        self.Goal4.setObjectName("Goal4")
        
        #Goal 5 - move base
        self.Goal5 = QtWidgets.QPushButton(self.frame_3)
        self.Goal5.setGeometry(QtCore.QRect(90, 250, 89, 25))
        self.Goal5.setObjectName("Goal5")
        
        #Send Goal - move base
        self.SendGoal = QtWidgets.QPushButton(self.frame_3)
        self.SendGoal.setGeometry(QtCore.QRect(10, 330, 111, 41))
        self.SendGoal.setObjectName("SendGoal")
        
        #Kill - move base
        self.Kill = QtWidgets.QPushButton(self.frame_3)
        self.Kill.setGeometry(QtCore.QRect(140, 330, 111, 41))
        self.Kill.setObjectName("Kill")
        
        #Dynamic label - Displays current goal selected
        self.goallabel = QtWidgets.QLabel(self.frame_3)
        self.goallabel.setGeometry(QtCore.QRect(90, 290, 111, 20))
        self.goallabel.setText("")
        self.goallabel.setObjectName("goallabel")
        
        # Start button
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(20, 420, 121, 51))
        self.start.setObjectName("start")
        
        # Pause button
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(160, 420, 121, 51))
        self.pause.setObjectName("pause")
        
        # Stop button
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(300, 420, 121, 51))
        self.stop.setObjectName("stop")

        
        #Setting up menu and status bars
        Navigation_Task.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Navigation_Task)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 22))
        self.menubar.setObjectName("menubar")
        Navigation_Task.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Navigation_Task)
        self.statusbar.setObjectName("statusbar")
        Navigation_Task.setStatusBar(self.statusbar)

        self.retranslateUi(Navigation_Task)
        QtCore.QMetaObject.connectSlotsByName(Navigation_Task)

    def retranslateUi(self, Navigation_Task):
        _translate = QtCore.QCoreApplication.translate
        Navigation_Task.setWindowTitle(_translate("Navigation_Task", "Leorover_MRM control panel"))
        
        # capture center
        self.capture.setText(_translate("Navigation_Task", "capture"))
        self.capture.clicked.connect(self.image)
        
        # capture left
        self.capture_left.setText(_translate("Navigation_Task", "capture left "))
        self.capture_left.clicked.connect(self.image_left)
        
        # capture right
        self.capture_right.setText(_translate("Navigation_Task", "capture right "))
        self.capture_right.clicked.connect(self.image_right)
        
        # probe deployment callback
        self.probe.setText(_translate("Navigation_Task", "Deploy Probe"))
        self.probe.clicked.connect(self.deploy)
        
        # Individual Goal Callbacks
        self.Goal1.setText(_translate("Navigation_Task", "Goal 1"))
        self.Goal1.clicked.connect(self.sendgoal1)
        
        self.Goal2.setText(_translate("Navigation_Task", "Goal 2"))
        self.Goal2.clicked.connect(self.sendgoal2)
        
        self.Goal3.setText(_translate("Navigation_Task", "Goal 3"))
        self.Goal3.clicked.connect(self.sendgoal3)
        
        self.Goal4.setText(_translate("Navigation_Task", "Goal 4"))
        self.Goal4.clicked.connect(self.sendgoal4)

        self.Goal5.setText(_translate("Navigation_Task", "Goal 5"))
        self.Goal5.clicked.connect(self.sendgoal5)

        
        # Submitting Goal Callback
        self.SendGoal.setText(_translate("Navigation_Task", "Send Goal"))
        self.SendGoal.clicked.connect(self.submit)
        
        # Kill Node Callback
        self.Kill.setText(_translate("Navigation_Task", "Kill"))
        self.Kill.clicked.connect(self.kill)
        
        # Start callback
        self.start.setText(_translate("Navigation_Task", "Start "))
        
        # Pause callback
        self.pause.setText(_translate("Navigation_Task", "Pause"))
        
        # Stop callback
        self.stop.setText(_translate("Navigation_Task", "Stop"))
        self.stop.clicked.connect(self.stop_nav)

        # LABELS
        self.label.setText(_translate("Navigation_Task", "Take images"))
        self.counter.setText(_translate("Navigation_Task", "0"))
        self.mlabel.setText(_translate("Navigation_Task", "Press to deliver move_base goals"))
        self.goallabel.setText(_translate("Navigation_Task", " "))

         
    def image(self):
        os.system('rosservice call /capture_image/save')
        print ("saved image from central camera")
    
    def image_left(self):
        os.system('rosservice call /capture_image_left/save')
        print ("saved image from left camera")
    
    def image_right(self):
        os.system('rosservice call /capture_image_right/save')
        print ("saved image from right camera")

    def stop_nav(self):
        os.system('rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}')
        print ("Cancelling Move Base Goal")
    
    
    def deploy(self):
        self.counter_probe += 1
        os.system('rosrun leo_erc_gazebo waypoint_probe_deployment.py')
        if self.counter_probe <= 5:
            self.counter.setText(str(self.counter_probe))
            
    
        # Callback Functions to send goals
    def sendgoal1(self):
        self.goalno = "goal1"
        #os.system('rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}')
        print("Goal 1 selected")
        _translate = QtCore.QCoreApplication.translate
        self.goallabel.setText(_translate("Navigation_Task", "Goal 1 selected"))

    def sendgoal2(self):
        self.goalno = "goal2"
        #os.system('rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}')
        print("Goal 2 selected")
        _translate = QtCore.QCoreApplication.translate
        self.goallabel.setText(_translate("Navigation_Task", "Goal 2 selected"))

    def sendgoal3(self):
        self.goalno = "goal3"
        #os.system('rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}')
        print("Goal 3 selected")
        _translate = QtCore.QCoreApplication.translate
        self.goallabel.setText(_translate("Navigation_Task", "Goal 3 selected"))

    def sendgoal4(self):
        self.goalno = "goal4"
        #os.system('rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}')
        print("Goal 4 selected")
        _translate = QtCore.QCoreApplication.translate
        self.goallabel.setText(_translate("Navigation_Task", "Goal 4 selected"))

    def sendgoal5(self):
        self.goalno = "goal5"
        #os.system('rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}')
        print("Goal 5 selected")
        _translate = QtCore.QCoreApplication.translate
        self.goallabel.setText(_translate("Navigation_Task", "Goal 5 selected"))

        # Callback Functions for submit
    def submit(self):
        self.decide()
        # Left empty for scope of adding more features
   

        # Callback Functions to publish goals to move_base node
    def decide(self):
        print("Submitting")
        _translate = QtCore.QCoreApplication.translate
        self.goallabel.setText(_translate("Navigation_Task", "...Submitting"))
        self.nav_goal.target_pose.header.frame_id = "map"
        self.nav_goal.target_pose.header.stamp = rospy.Time.now()
        self.nav_goal.target_pose.pose.position.x = self.goals_erc[self.goalno][0]
        self.nav_goal.target_pose.pose.position.y = self.goals_erc[self.goalno][1]
        self.nav_goal.target_pose.pose.position.z = self.goals_erc[self.goalno][2]
        self.nav_goal.target_pose.pose.orientation.x = self.goals_erc[self.goalno][3]
        self.nav_goal.target_pose.pose.orientation.y = self.goals_erc[self.goalno][4]
        self.nav_goal.target_pose.pose.orientation.z = self.goals_erc[self.goalno][5]
        self.nav_goal.target_pose.pose.orientation.w = self.goals_erc[self.goalno][6]
        print(self.nav_goal)
        self.client.send_goal(self.nav_goal)

    def kill(self):
        rospy.signal_shutdown("Node Killed!!")
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    rospy.init_node("GUI")
    app = QtWidgets.QApplication(sys.argv)
    Navigation_Task = QtWidgets.QMainWindow()
    ui = Ui_Navigation_Task()
    ui.setupUi(Navigation_Task)
    Navigation_Task.show()
    sys.exit(app.exec_())



