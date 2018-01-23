#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from tuling import *
from is_cmd import *
from recognize import recognize
import subprocess
import thread


def callback(data,args):
    rospy.loginfo(rospy.get_caller_id() + 'Handler rcv  %s', data.data)
    
    cmd = run_cmd(data.data)
    if cmd == None:
    	answer = jsonPost(data.data)
    	args[0].publish("ok")
        print("say something")
    else:
        rospy.loginfo(rospy.get_caller_id() + 'Twist %s', data.data)
        para = cmd
        r = rospy.Rate(100)
        if len(para)==3:
        	cmd = Twist()
        	cmd.linear.x,cmd.angular.z =para[:2]
        	for i in range(0,1000*para[2]):
			args[1].publish(cmd)
			r.sleep()



def listener():
    #rospy.init_node('speech_handler', anonymous=True)
    m = subprocess.Popen(["rosrun", "xfei_asr", "iat_publish_speak"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    i = subprocess.Popen(["rostopic", "echo", "/xfword"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    j = subprocess.Popen(["rostopic", "echo", "/speech"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    pub = rospy.Publisher('/xfwords', String, queue_size=10)
    pub2 = rospy.Publisher('/mobile_base/commands/velocity', Twist,queue_size=10) 
    rospy.Subscriber('/xfspeech', String, callback,(pub,pub2))
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('lstener_interation', anonymous=True)
    listener()
#    rate = rospy.Rate(1)
#    while not rospy.is_shutdown():
#        listener()
#        print("listen")
#        rate.sleep()   
    

