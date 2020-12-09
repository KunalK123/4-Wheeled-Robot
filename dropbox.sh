rosservice call gazebo/delete_model robot
rosservice call gazebo/delete_model final_setup
rosservice call gazebo/delete_model final_setup_test
rosrun gazebo_ros spawn_model -file final_test.sdf -sdf -model final_setup_test -y -0.0 -x -0.0 -z 0.0
rosrun gazebo_ros spawn_model -file final.sdf -sdf -model final_setup -y -0.0 -x -0.0 -z 0.0
rosrun gazebo_ros spawn_model -file box.sdf -sdf -model robot -y 0.0 -x 0.0 -z 15.0
