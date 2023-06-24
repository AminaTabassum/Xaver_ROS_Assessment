#!/usr/bin/env python3

import rospy
import tf
from geometry_msgs.msg import Twist

# Follower turtle class
class leader_follower_turtle:
    def __init__(self):
        rospy.init_node('leader_follower_turtles')
        self.listener = tf.TransformListener()
        self.follower_pub = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1)
        self.leader = 'turtle1'
        self.follower = 'turtle2'
        self.distance_to_be_maintained = 0.8

    def turtle2_follower_turtle1(self):
        rate = rospy.Rate(10)  # 10 Hz

        while not rospy.is_shutdown():
            try:
                # Get the transform between the leader and follower turtle
                (translation, rot) = self.listener.lookupTransform(self.leader, self.follower, rospy.Time(0))
                
                # Calculate the vector from the leader to the follower
                leader_to_follower = [translation[0], translation[1]]

                # Calculate the current distance_to_be_maintained between the leader and follower
                current_distance_to_be_maintained = self.calculate_distance_to_be_maintained(leader_to_follower)

                # Calculate the desired distance_to_be_maintained behind the leader
                desired_distance_to_be_maintained = current_distance_to_be_maintained + self.distance_to_be_maintained

                # Calculate the desired position for the follower turtle
                desired_position = self.calculate_desired_position(leader_to_follower, desired_distance_to_be_maintained)

                # Calculate the desired velocity for the follower turtle
                desired_velocity = self.calculate_desired_velocity(desired_position)

                # Publish the desired velocity as Twist message to control the follower turtle
                self.publish_velocity(desired_velocity)

            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue

            rate.sleep()

    def calculate_distance_to_be_maintained(self, vector):
        return ((vector[0])**2 + (vector[1])**2)**0.5

    def calculate_desired_position(self, vector, distance_to_be_maintained):
        magnitude = (vector[0]**2 + vector[1]**2)**0.5
        unit_vector = [vector[0]/magnitude, vector[1]/magnitude]
        desired_position = [vector[0] + unit_vector[0]*distance_to_be_maintained, vector[1] + unit_vector[1]*distance_to_be_maintained]
        return desired_position

    def calculate_desired_velocity(self, desired_position):
        desired_velocity = Twist()
        desired_velocity.linear.x = (desired_position[0] - 0)
        desired_velocity.linear.y = (desired_position[1] - 0)
        return desired_velocity

    def publish_velocity(self, velocity):
        self.follower_pub.publish(velocity)


if __name__ == '__main__':
    try:
        follower_turtle = leader_follower_turtle()
        follower_turtle.turtle2_follower_turtle1()
    except rospy.ROSInterruptException:
        pass
