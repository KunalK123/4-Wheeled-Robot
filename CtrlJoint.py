#!/usr/bin/env python3
import rospy
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
import os
import time as t

msg_topic = '/gazebo/apply_joint_effort'
joint_left_front = 'left_wheel_hinge_front'
joint_right_front = 'right_wheel_hinge_front'
joint_left_back = 'left_wheel_hinge_back'
joint_right_back = 'right_wheel_hinge_back'

msg_topic_feedback = 'gazebo/get_joint_properties'

pub_feedback = rospy.ServiceProxy(msg_topic_feedback, GetJointProperties)

rospy.init_node('dd_ctrl')
pub = rospy.ServiceProxy(msg_topic,ApplyJointEffort)

effort_right = 0.5
effort_left = 0.5
start_time = rospy.Time(0,0)

f = 0.25
T = 1/f
end_time = rospy.Time(T,0)
rate = rospy.Rate(f)

#my_service = rospy.Service('/service_example_topic', Trigger, trigger_response)

robot_proxy = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

while True:
      x = 0
      z = raw_input("Input:")
      global robot_proxy
      a = GetModelStateRequest(model_name = 'robot')
      a.model_name = "robot"
      s = robot_proxy(a)
      x = s.pose.position.x
      y = s.pose.position.y
      
      if(z == 'w'):
        effort_left = effort_left
        effort_right = effort_right
        pub(joint_left_front, effort_left, start_time, end_time)
        pub(joint_right_front, effort_right, start_time, end_time)
        pub(joint_left_back, effort_left, start_time, end_time)
        pub(joint_right_back, effort_right, start_time, end_time)
        print(s)

      if(z == 's'):
        effort_left = -effort_left
        effort_right = -effort_right
        pub(joint_left_front, effort_left, start_time, end_time)
        pub(joint_right_front, effort_right, start_time, end_time)
        pub(joint_left_back, effort_left, start_time, end_time)
        pub(joint_right_back, effort_right, start_time, end_time)
        print(s)
            
      if(z == 'a'):
        effort_left = 2.5
        effort_right = -1
        pub(joint_left_front, 0, start_time, end_time)
        pub(joint_right_front, effort_right, start_time, end_time)
        pub(joint_left_back, effort_left, start_time, end_time)
        pub(joint_right_back, 0, start_time, end_time)
        print(s)
      
      if(z == 'd'):
        effort_left = -1
        effort_right = 2.5
        pub(joint_left_front, effort_left, start_time, end_time)
        pub(joint_right_front, 0, start_time, end_time)
        pub(joint_left_back, 0, start_time, end_time)
        pub(joint_right_back, effort_right, start_time, end_time)
        print(s)

      if(z == 'r'):
        effort_left = 0
        effort_right = 0
        pub(joint_left_front, effort_left, start_time, end_time)
        pub(joint_right_front, 0, start_time, end_time)
        pub(joint_left_back, 0, start_time, end_time)
        pub(joint_right_back, effort_right, start_time, end_time)
        print(s)
