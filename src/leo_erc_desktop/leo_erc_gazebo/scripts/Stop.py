#!/usr/bin/env python2
#Importing required Packages
import rospy
from nav_msgs.msg import Odometry
from move_base_msgs.msg import MoveBaseActionGoal,MoveBaseGoal
import math
import numpy as np 
import time
import actionlib
from actionlib_msgs.msg import GoalStatusArray,GoalID
import os

class Cancel:
	def __init__(self):
		self.goal_x =0
		self.goal_y=0
		self.odom_x =0
		self.odom_y=0
		self.dist =0
		self.status=0
		self.flag = False
		self.pub = rospy.Publisher('/move_base/cancel',GoalID,queue_size=10)
		self.sub_stat = rospy.Subscriber('/move_base/status',GoalStatusArray , self.getstat)
		self.sub_odom = rospy.Subscriber('/rtabmap/odom', Odometry, self.getodom)		
		self.sub_goal = rospy.Subscriber('/move_base/goal', MoveBaseActionGoal, self.getgoal)

	def getgoal(self,msg):
		self.goal_x = msg.goal.target_pose.pose.position.x 
		self.goal_y = msg.goal.target_pose.pose.position.y 
		print("Received new goal {} , {} ".format(self.goal_x,self.goal_y))
	
	def getodom(self,odom):
		self.odom_x= odom.pose.pose.position.x 
		self.odom_y= odom.pose.pose.position.y
		self.dist = math.sqrt((self.odom_x-self.goal_x)**2+(self.odom_y-self.goal_y)**2)
		print("Distance from goal : {}".format(self.dist))
		if (not self.flag):
			self.flag = self.check()
		if(self.flag):
			goal = GoalID()
			self.pub.publish(goal)
			print("Reached Goal, Sent cancel command")
			self.flag=False

	def check(self):
		if(self.status == 0):
			print("Waiting for goal to be set")
		elif(self.status != 2):
			print("Movig towards goal")
		if (self.dist<0.5 and self.status !=0):
			return True
		return False

	def getstat(self,stat):
		self.status = stat.status_list[0].status
			

if __name__ == '__main__':
    rospy.init_node('Cancel')
    Cancel()
    rospy.spin()
