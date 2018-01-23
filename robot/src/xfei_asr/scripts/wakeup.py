#!usr/bin/env python

import rospy
from std_msgs.msg import String
import subprocess

if __name__=="__main__":
    rospy.init_node('wake_listener',anonymous=True)
    rate = rospy.Rate(0.2)
    s = subprocess.Popen(["rostopic", "echo", "/xfwakeup"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    pub_wake = rospy.Publisher('/xfwakeup', String, queue_size=2)
    while not rospy.is_shutdown():
        pub_wake.publish("ok")
        rate.sleep()
