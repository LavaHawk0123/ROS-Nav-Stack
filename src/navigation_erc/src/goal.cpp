
#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <iostream>
 
using namespace std;
 

typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;
 
int main(int argc, char** argv){
   
  // Connect to ROS
  ros::init(argc, argv, "simple_navigation_goals");
 
  //tell the action client that we want to spin a thread by default
  MoveBaseClient ac("move_base", true);
 
  // Wait for the action server to come up so that we can begin processing goals.
  while(!ac.waitForServer(ros::Duration(5.0))){
    ROS_INFO("Waiting for the move_base action server to come up");
  }
 
  int user_choice = 6;
  char choice_to_continue = 'Y';
  bool run = true;
  std::list<float> erc_goals ;
  //ros::param::get("/goals",erc_goals);
     
  while(run) {
 
    // Ask the user where he wants the robot to go?
    cout << "\nWhere do you want the robot to go?" << endl;
    cout << "\nEnter a number: ";
    cin >> user_choice;
    // Create a new goal to send to move_base 
    move_base_msgs::MoveBaseGoal goal;
 
    // Send a goal to the robot
    goal.target_pose.header.frame_id = "map";
    goal.target_pose.header.stamp = ros::Time::now();
         
    bool valid_selection = true;
    goal.target_pose.pose.orientation.x = 0.00;
    goal.target_pose.pose.orientation.y = 0.00;
    goal.target_pose.pose.orientation.z = 0.377;
    goal.target_pose.pose.orientation.w = 0.926;
 
    // Use map_server to load the map of the environment on the /map topic. 
    // Launch RViz and click the Publish Point button in RViz to 
    // display the coordinates to the /clicked_point topic.
    switch (user_choice) {
      case 1:
        cout << "\nGoal Location: 1\n" << endl;
        goal.target_pose.pose.position.x = 12.19;
        goal.target_pose.pose.position.y = 8.73;
        goal.target_pose.pose.position.z = 0.271;
        break;
      case 2:
        cout << "\nGoal Location: 2\n" << endl;
        goal.target_pose.pose.position.x = 25.54;
        goal.target_pose.pose.position.y = 4.36;
        goal.target_pose.pose.position.z = 0.271;
        break;
      case 3:
        cout << "\nGoal Location: 3\n" << endl;
        goal.target_pose.pose.position.x = 28.62;
        goal.target_pose.pose.position.y = -6.17;
        goal.target_pose.pose.position.z = 0.271;

        break;
      case 4:
        cout << "\nGoal Location: 4\n" << endl;
        goal.target_pose.pose.position.x = 11.63;
        goal.target_pose.pose.position.y = -16.85;
        goal.target_pose.pose.position.z = 0.272;
        break;
      case 5:
        cout << "\nGoal Location: 5\n" << endl;
        goal.target_pose.pose.position.x = 7.64;
        goal.target_pose.pose.position.y = -5.55;
        goal.target_pose.pose.position.z = 0.271;
        break;
      case 6:
        cout << "\nGoal Location: 6\n" << endl;
        goal.target_pose.pose.position.x = 27.48;
        goal.target_pose.pose.position.y = -13.65;
        goal.target_pose.pose.position.z = 0.272;
        break;
      default:
        cout << "\nInvalid selection. Please try again.\n" << endl;
        valid_selection = false;
    }       
         
    // Go back to beginning if the selection is invalid.
    if(!valid_selection) {
      continue;
    }
 
    ROS_INFO("Sending goal");
    ac.sendGoal(goal);
 
    // Wait until the robot reaches the goal
    ac.waitForResult();
 
    if(ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
      ROS_INFO("The robot has arrived at the goal location");
    else
      ROS_INFO("The robot failed to reach the goal location");
         
    // Ask the user if he wants to continue giving goals
    do {
      cout << "\nWould you like to go to another destination? (Y/N)" << endl;
      cin >> choice_to_continue;
      choice_to_continue = tolower(choice_to_continue); // Put your letter to its lower case
    } while (choice_to_continue != 'n' && choice_to_continue != 'y'); 
 
    if(choice_to_continue =='n') {
        run = false;
    }  
  }
   
  return 0;
}