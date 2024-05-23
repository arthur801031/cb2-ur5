import urx
import time

if __name__ == '__main__':
    robot_left = urx.Robot("192.10.0.11")
    joints_left = robot_left.getj()
    print('Left robot joints: ', joints_left)
    time.sleep(1)

    robot_right = urx.Robot("192.10.0.12")
    joints_right = robot_right.getj()
    print('Right robot joints: ', joints_right)

    # starting states for our robots in GELLO and real-world experiments
    starting_robot_joints_left = [1.5830758046519644, -1.506298391828153, -1.6138142421812975, -1.5579707136319096, 1.6942172572292165, -0.0340714387454657]
    starting_robot_joints_right = [-1.6319297499480427, -1.5404013477690743, 1.693556168958768, -1.8420827585266242, -1.7180060512420487, -0.03545634775981554]

    for i in range(100):
        robot_left.servoj(
            starting_robot_joints_left, vel=0.1, acc=0.3, t=0.35, lookahead_time=0.2, gain=100, wait=False
        )
    time.sleep(1)
    print('Finished moving the left arm to starting states.')

    for i in range(100):
        robot_right.servoj(
            starting_robot_joints_right, vel=0.1, acc=0.3, t=0.35, lookahead_time=0.2, gain=100, wait=False
        )
    time.sleep(1)
    print('Finished moving the right arm to starting states.')
    print('Done')
