cmake_minimum_required(VERSION 3.0.2)
project(leo_erc_gazebo)

find_package(catkin REQUIRED)

catkin_package()

install(
  DIRECTORY
    config
    launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(
  PROGRAMS
    scripts/odom_compat_node
    scripts/zed2_imu_transform_broadcaster
    scripts/pdu_node
    scripts/drop.py
    scripts/wheel_odom_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
