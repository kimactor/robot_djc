#!/usr/bin/env python
#coding=utf-8
import re, subprocess
from recognize import recognize
import threading
fellow_process = None
#global exitFlag
#class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter,exitFlag):
#        threading.Thread.__init__(self)
#        self.threadID = threadID
#        self.name = name
#        self.counter = counter
#        self.exitFlag = exitFlag
#    def run(self)
#        startvision(self.name,self.exitFlag)
#def startvision(threadName,exitFlag):
#    if exitFlag== 1:
#        recognize()
#    else:
#	return 0
    
      

def get_length(string):
	num_pattern = re.compile(r'一|二|三|四|五|六|七|八|九|十')
	float_pattern = re.compile(r'[0-9]*\.[0-9]')
	match = num_pattern.search(string)
	if match != None:
		return {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}[match.group()]
	match = float_pattern.search(string)
	if match != None:
		return float(match.group())
	return None

def run_cmd(string):
       # thread1 = myThread(1, "vision",1,1)
	pattern = re.compile(r'你好|左|右|前|后|自己玩|回来|检测举手|跟|圈|加|减|停')
	match = pattern.search(string)
	global bringup_process
	global fellow_process
	global gmapping_process
	global exploration_process
	if match == None:
		return None
	elif match.group() == '你好':
		bringup_process = subprocess.Popen(["roslaunch", "turtlebot_exploration_3d", "minimal_explo.launch"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		gmapping_process = subprocess.Popen(["roslaunch", "turtlebot_exploration_3d", "turtlebot_gmapping.launch"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		screen_process = subprocess.Popen(["roslaunch", "turtlebot_exploration_3d", "exploration_rviz.launch"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                i = subprocess.Popen(["rosrun", "xfei_asr", "welcome.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return None
	elif match.group() == '左':
		#thread1.exitFlag = 1
                #thread1.start()
                #thread.start_new_thread(recognize,())
		length = get_length(string)
		if length != None:
			return (0.1,3,length)

	elif match.group() == '右':
		#thread.join()
                length = get_length(string)
		return (0.1,-3,length)
		

	elif match.group() == '前':
                #thread1.stop()
		#thread1.exitFlag = 0
		length = get_length(string)
		return (0.1,0,length)
		

	elif match.group() == '后':
		length = get_length(string)
		return (-0.1,0,length)
				
	elif match.group() == '自己玩':
		exploration_process = subprocess.Popen(["rosrun", "turtlebot_exploration_3d", "turtlebot_exploration_3d"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return None

	elif match.group() == '回来':
		if exploration_process != None:
			exploration_process.terminate()
			exploration_process = None
			return None
		else:
			return (0,0,0)
	elif match.group() == '跟':
		fellow_process = subprocess.Popen(["roslaunch", "turtlebot_follower", "follower.launch"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return None
	elif match.group() == '圈':
		length = get_length(string)
		return (0.1,0.3,length)
		

	elif match.group() == '加':
		return (2,)

	elif match.group() == '减':
		return (0.5,)

	elif match.group() == '停':
		if bringup_process != None:
			#fellow_process.terminate()
			bringup_process.terminate()
			#fellow_process = None
			bringup_process = None
			return None
		else:
			return (0,0,0)
