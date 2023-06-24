#include <ros/ros.h>
#include <std_msgs/Int8.h>
#include <geometry_msgs/PoseStamped.h>

ros::Publisher goal_pub;

void goalLocationCallback(const std_msgs::Int8::ConstPtr& msg)
{
    geometry_msgs::PoseStamped goal_msg;
    goal_msg.header.frame_id = "map";  

    int goal_location_id = msg->data;

    
    switch (goal_location_id)
    {
        case 1:
        // x,y coordinates for location 1
            goal_msg.pose.position.x = 1.0;   
            goal_msg.pose.position.y = 1.0;   
            break;
        case 2:
         // x,y coordinates for location 2
            goal_msg.pose.position.x = 2.0;   
            goal_msg.pose.position.y = 2.0;   
            break;
        case 3:
         // x,y coordinates for location 3
            goal_msg.pose.position.x = 3.0;   
            goal_msg.pose.position.y = 3.0;   
            break;
        default:
            ROS_WARN("Invalid goal location :", goal_location_id);
            return;  
    }

    goal_pub.publish(goal_msg);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "goal_location_subscriber");
    ros::NodeHandle nh;

    goal_pub = nh.advertise<geometry_msgs::PoseStamped>("/move_base_simple/goal", 1);
    ros::Subscriber goal_sub = nh.subscribe("/goal_location", 1, goalLocationCallback);

    ros::spin();

    return 0;
}

