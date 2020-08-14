#!/usr/bin/env python
#coding=utf-8
import rospy
import math
#导入mgs到pkg中
from listen_and_talk.msg import gps

#回调函数输入的应该是msg
def callback(gps):
    distance = math.sqrt(math.pow(gps.x, 2)+math.pow(gps.y, 2)) 
    rospy.loginfo('Listener: GPS: distance=%f, state=%s', distance, gps.state)

def message_node():
    #根据模块名, 修改Publisher 函数第一个参数
    rospy.init_node('node_template', anonymous=True)
    #Subscriber函数第一个参数是接收目标topic的名称,Publisher则对应自身发送topic的名称
    sub = rospy.Subscriber('gps_info', gps, callback)
    pub = rospy.Publisher('gps_info', gps , queue_size=10)
    #更新频率
    rate = rospy.Rate(10) 
    x=1.0
    y=2.0
    state='working'
    while not rospy.is_shutdown():
        #下面是一个例子
        rospy.loginfo('Talker: GPS: x=%f ,y= %f',x,y)
        pub.publish(gps(state,x,y))
        x=1.03*x
        y=1.01*y
        rate.sleep()

if __name__ == '__main__':

    message_node()

