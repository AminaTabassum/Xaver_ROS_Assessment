# Xaver_Assessment

**Question 1**
**Task 1**

1. Git clone this repositery using git clon git@github.com:AminaTabassum/Xaver_ROS_Assessment.git
2. source /opt/ros/noetic/setup.bash to source ros noetic bash file
3. source devil/setup.bash
4. cd src/xaver
5. roslaunch turtle.launch

**Task 2**
1. Open a new terminal 
2. source /opt/ros/noetic/setup.bash to source ros noetic bash file
3. source devil/setup.bash
4. cd src/xaver
5. roslaunch leader_follower.launch


**Question 02**
**Task 1**
1. cd xaver_ws
2. source /opt/ros/noetic/setup.bash
3. source devel/setup.bash
4. cd src
5. git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
6. cd ../
7. catkin_make
8. export TURTLEBOT3_MODEL=burger
9. roslaunch turtlebot3_gazebo turtlebot3_world.launch
10. roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
11. Launch Slam and teleoperation node to create map.
12. Open a new terminal and source package workspace
13.  export TURTLEBOT3_MODEL=burger
14.  roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
15.  Open a new terminal
16.  export TURTLEBOT3_MODEL=burger
17.  roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
18.  Create the map of the environment and save it.
19.  rosrun map_server map_saver -f ~/task2
20.  Open a new terminal and start navigation node
21.  export TURTLEBOT3_MODEL=burger
22.  roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/task2.yaml
23.  CLick on 2D pose estimate to estimate intial pose
24.  Click on 2D Nav Goal to set goal
For this task , open task2.rviz file . Estimate  initial pose and set navigation goal. The robot plans and starts navigating. You can find  sample navigation videos 1.webm and 2.webm of the pose estimation, goal and turtlesim navigation in this package.

**Task 2**
 This is simple task and you can run this file q2.cpp using rosrun command as 
 rosrun  xaver q2.cpp 
 where xaver is package name.


