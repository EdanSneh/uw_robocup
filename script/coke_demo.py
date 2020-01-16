#! /usr/bin/env python
from arm import Arm
#from . import arm_joints
from head import Head
import rospy
from moveit_python import PlanningSceneInterface
from geometry_msgs.msg import PoseStamped
from moveit_msgs.msg import OrientationConstraint

def wait_for_time():
    """Wait for simulated time to begin.
    """
    while rospy.Time().now().to_sec() == 0:
        pass

def main():
    rospy.init_node('coke_demo')
    wait_for_time()
    h = Head()
    h.pan_tilt(0, .7)
    
    pose1 = PoseStamped()
    pose1.header.frame_id = 'base_link'
    pose1.pose.position.x = 0.5
    pose1.pose.position.y = -0.3
    pose1.pose.position.z = 0.75
    pose1.pose.orientation.w = 1
    a = Arm()
    a.move_to_pose(pose1)

if __name__ == '__main__':
    main()