# Space Robotics Workshop

## List of commands:

<ul>
  <li>mkdir &lt;name&gt; - Creates directories (folders) in your system with the same name</li>
  <li>catkin_make - Automatically builds your workspace</li>
  <li>source devel/setup.bash - Adds and updates our workspace in the ROS environment</li>
  <li>catkin_create_pkg &lt;name&gt; &lt;dependencies&gt; - Creates a catkin package</li>
  <li>chmod +x &lt;filename&gt; - Gives a file executable permissions</li>
  <li>rosrun &lt;package name&gt; &lt;filename&gt; - Finds a file and executes it</li>
  <li>rostopic list - Gives a list of all the active topics</li>
  <li>roscore - You must have a roscore running in order for ROS nodes to communicate.</li>
  </ul>

## Steps to run Turtlebot3 simulation in Gazebo:
  1. Creation of folders:
```
 $ mkdir -p ~/<name>/src
 $ cd name ~/<name>
```
2. Building a [catkin workspace](http://wiki.ros.org/catkin/workspaces):
```
$ catkin_make
```
3. Installing Turtlebot3 and Gazebo:
```
$ sudo apt-get update
$ sudo apt-get install ros-noetic-turtlebot3-*
$ echo “export TURTLEBOT3_MODEL=waffle_pi” >> ~/.bashrc
$ sudo apt-get install ros-noetic-gazebo-*
```
4. Launching an empty simulation:
```
$ roscore
$ roslaunch turtlebot3_gazebo 
$ turtlebot3_empty_world.launch
```
5. Have fun :D
