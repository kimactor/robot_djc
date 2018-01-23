#!/usr/bin/env python
#coding=utf-8
from urllib import urlopen
import rospy
from std_msgs.msg import String
from kobuki_msgs.msg import Led
from kobuki_msgs.msg import Sound
from geometry_msgs.msg import Twist
from recognize import * 
import thread

def get_state():
    x = int(urlopen("http://vpn.holoshadow.cn:8080/state").read())
    return x

def get_record():
    x = int(urlopen("http://vpn.holoshadow.cn:8080/record").read())
    return x

def reset():
    x = int(urlopen("http://vpn.holoshadow.cn:8080/reset").read())
    return x

if __name__=="__main__":    
    rospy.init_node('Mobile_Control', anonymous=True)
    sound_pub = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size = 10)
    wake_pub = rospy.Publisher('xfwakeup', String, queue_size = 2)
    speech_pub = rospy.Publisher('xfspeech',String, queue_size = 2)
    rate = rospy.Rate(1) # 10hz
    try:        
        while not rospy.is_shutdown():
            if(get_record()==1):
                sound_pub.publish(6)
                wake_pub.publish("ok")
                recognize()
                #thread.start_new_thread(reset,())
                reset()
            if(get_state()!=0):
                sound_pub.publish(3)
                x = get_state()
                y = ['','前进一米','后退一米','左转一米','右转一米']
                speech_pub.publish(y[x])
                reset()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass

