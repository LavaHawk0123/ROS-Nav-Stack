#include "ros/ros.h"
#include "std_msgs/UInt8.h"
#include "std_msgs/Empty.h"
#include "geometry_msgs/Twist.h"


class probe_deploy
{
	public:
	ros::Publisher pub;
    ros::Subscriber sub;

    probe_deploy(ros::NodeHandle *n)
    {
        pub = n->advertise<std_msgs::Empty>("/probe_deployment_unit/drop", 1);
        sub = n->subscribe("/probe_deployment_unit/probes_dropped",1000, &probe_deploy::drop_probe,this);
    }

    void drop_probe(const std_msgs::UInt8::ConstPtr& msg);
};

void probe_deploy::drop_probe(const std_msgs::UInt8::ConstPtr& msg)
{
    std_msgs::Empty data;
    int i = 0;
    while (i < 6)
    {
        if (i >= msg->data + 1)
            ros::shutdown();      
        pub.publish(data);
        i = msg->data + 1;
    }
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "map_maker");
    ros::NodeHandle n;
    probe_deploy ob=probe_deploy(&n);
    ros::spin();
    return 0;
}

