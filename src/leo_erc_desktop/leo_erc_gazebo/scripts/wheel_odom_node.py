#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import TwistWithCovarianceStamped,TwistWithCovariance,TwistStamped,PoseStamped
from std_msgs.msg import Header, String

import numpy

class wheelodom:
    def __init__(self):
    
        self.twist_data = TwistWithCovarianceStamped()
        rospy.Subscriber('/wheel_odom', TwistStamped, self.twist_callback)
        self.pub = rospy.Publisher('/wheel_odometry', TwistWithCovarianceStamped, queue_size=10)
        self.rate = rospy.Rate(10)

        self.rate.sleep()

    def twist_callback(self, data):
        self.twist_data.header=data.header;
        self.twist_data.twist.covariance = [0.0001,0.0,0.0,0.0,0.0,0.0,
                                        0.0,0.0,0.0,0.0,0.0,0.0,
                                        0.0,0.0,0.0,0.0,0.0,0.0,
                                        0.0,0.0,0.0,0.0,0.0,0.0,
                                        0.0,0.0,0.0,0.0,0.0,0.0,
                                        0.0,0.0,0.0,0.0,0.0,0.001]
        self.twist_data.twist.twist = data.twist;
        self.pub.publish(self.twist_data);

while not rospy.is_shutdown():
    rospy.init_node('wheel_odom_combined')
    wheelodom()
    
