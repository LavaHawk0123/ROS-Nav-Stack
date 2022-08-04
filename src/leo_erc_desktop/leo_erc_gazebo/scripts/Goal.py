#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal
from std_msgs.msg import Empty
import actionlib
import math

class send_goal:
        
	def __init__(self):
        	self.goals_erc = rospy.get_param("/goals")
        	print(self.goals_erc)
		self.goal = str(input("Enter the goal no : "))
		self.goalno = "goal"+self.goal
        	self.nav_goal = MoveBaseGoal()
        	self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
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
		wait = self.client.wait_for_result()
    		# If the result doesn't arrive, assume the Server is not available
    		if not wait:
        		rospy.logerr("Action server not available!")
        		rospy.signal_shutdown("Action server not available!")
    		else:
        		# Result of executing the action
        		print(self.client.get_result())

if __name__ == "__main__":
	rospy.init_node('map_maker', anonymous = True)
	send_goal()
	
