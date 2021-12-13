#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import *
from gazebo_msgs.msg import ModelStates


position = Pose()

a = 0
time = 0

def position_callback(data):
	global position

	position = data.pose[-1]

	#print(position)

if __name__=="__main__":
	rospy.init_node("DESAFIO_NODE", anonymous=False)
    
	rospy.Subscriber("/gazebo/model_states", ModelStates, position_callback)
	
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size=20)
	r = rospy.Rate(10)
    
	velocity = Twist()

	while not rospy.is_shutdown():
    # vai de (0,0) a (1,0)	
		if a == 0:
			velocity.linear.x = 0.1

			if position.position.y < 0:
				velocity.angular.z = 0.1

			if position.position.y > 0:
				velocity.angular.z = -0.1	


			if position.position.x > 1.03:
				a = a + 1
				velocity.linear.x = 0
    # vai gira o carrinho
		if a == 1:
			velocity.linear.x = -0.1
			velocity.angular.z = 2
			time = time + 1
			if time == 10:
				a = a + 1
				time = 0

    #vai de (1,0) a (1,1)
		if a == 2:
			velocity.linear.x = 0.1

			if position.position.x > 1:
				velocity.angular.z = 0.1

			if position.position.x < 1:
				velocity.angular.z = -0.1	

			if position.position.y > 1.03:					
				a = a + 1
				velocity.linear.x = 0

    # vai gira o carrinho
		if a == 3:
			velocity.linear.x = -0.1
			velocity.angular.z = 2
			time = time + 1
			if time == 10:
				a = a + 1
				time = 0
    # vai de (1,1) a (0,1)
		rospy.loginfo("a: (%s)", a)
	
		if a == 4:
			velocity.linear.x = 0.1

			if position.position.y > 1:
				velocity.angular.z = 0.1

			if position.position.y < 1:
				velocity.angular.z = -0.1	


			if position.position.x < -0.03:
				a = a + 1
				velocity.linear.x = 0
    # vai gira o carrinho
		if a == 5:
			velocity.linear.x = 0
			velocity.angular.z = 2
			time = time + 1
			if time == 10:
				a = a + 1
				time = 0
		# vai de (0,1) a (0,0)

		if a == 6:
			velocity.linear.x = 0.1

			if position.position.x < 0:
				velocity.angular.z = 0.1

			if position.position.x > 0:
				velocity.angular.z = -0.1	

			if position.position.y < -0.03:					
				a = a + 1
				velocity.linear.x = 0

    # vai gira o carrinho
		if a == 7:
			velocity.linear.x = -0.1
			velocity.angular.z = 2
			time = time + 1
			if time == 10:
				a = 0
				time = 0
		pub.publish(velocity)

		rospy.loginfo("x: (%s) | y: (%s)", position.position.x, position.position.y)
		r.sleep()