#include "ros/ros.h"
#include "move_base_msgs/MoveBaseActionGoal.h"
#include "move_base_msgs/MoveBaseGoal.h"
#include "move_base_msgs/MoveBaseAction.h"
#include "actionlib_msgs/GoalStatusArray.h"
#include "actionlib/client/simple_action_client.h"


typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction>  MoveBaseClient;
int main (int argc, char** argv)
{
    ros::init(argc, argv, "send_goal");
    //std::list<float> erc_goals;
    ros::NodeHandle n;
    //ros::param::get("/goals", erc_goals);
    
    std::cout<< "Enter goal index: ";
    int goal_index=0;
	std::cin >> goal_index;
	//pub = n.advertise<actionlib_msgs::GoalID>("/move_base/", 10);
    move_base_msgs::MoveBaseGoal goal;
	std::cout<<"\n Goal no set : "<< goal_index<<"\n";
    goal.target_pose.header.frame_id = "map";
    goal.target_pose.header.stamp = ros::Time::now();
    goal.target_pose.pose.position.x = 2.39;
    goal.target_pose.pose.position.y = -1.59;
    goal.target_pose.pose.position.z = 0.00;
    goal.target_pose.pose.orientation.x = 0.00;
    goal.target_pose.pose.orientation.y = 0.00;
    goal.target_pose.pose.orientation.z = 0.377;
    goal.target_pose.pose.orientation.w = 0.926; 
    actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> ac("move_base", true);
    ac.sendGoal(goal);
    ros::spin();
    return 0;
}