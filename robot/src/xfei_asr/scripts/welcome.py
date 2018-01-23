#!/usr/bin/env python
from urllib import urlopen
import rospy
from std_msgs.msg import String
from kobuki_msgs.msg import Led
from kobuki_msgs.msg import Sound
from geometry_msgs.msg import Twist


if __name__=="__main__":    
    rospy.init_node('welcome', anonymous=True)
    sound_pub = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size = 10)
    led_pub = rospy.Publisher('mobile_base/commands/led1',Led,queue_size = 10)
    speech_pub = rospy.Publisher('xfspeech',String, queue_size = 2)
    rate = rospy.Rate(3) # 10hz
    i=0
    try:        
    	for i in range(15):
		i=i+1
    		led_pub.publish(((i)%3))
    		rate.sleep()
    except rospy.ROSInterruptException:
        pass

