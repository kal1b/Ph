cmake_minimum_required(VERSION 3.0.2)
project(parallel_planner)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  dynamic_reconfigure
  tf2_ros
  pcl_ros
)

catkin_package()

catkin_install_python(PROGRAMS
  src/kalman_filter_node.py
  src/dsm_node.py
  src/vfh_node.py
  src/parallel_planner_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
