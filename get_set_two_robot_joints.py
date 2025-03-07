import urx
import time

def slow_servoj_move(robot, q_target, steps=100):
    q_current = robot.getj()
    
    for i in range(steps):
        q_interp = [(1 - i/steps) * q_current[j] + (i/steps) * q_target[j] for j in range(6)]
        try:
            robot.servoj(q_interp, vel=0.001, acc=0.003, t=0.1, lookahead_time=0.2, gain=10, wait=False)
        except:
            pass

if __name__ == '__main__':
    robot_left = urx.Robot("192.10.0.12")
    joints_left = robot_left.getj()
    print('Left robot joints: ', joints_left)
    time.sleep(1)

    robot_right = urx.Robot("192.10.0.11")
    joints_right = robot_right.getj()
    print('Right robot joints: ', joints_right)

    # starting states for our robots in GELLO and real-world experiments
    starting_robot_joints_left = [1.3780459778509433, -1.523749890442781, -1.5899893346228173, -1.523211104456275, 1.722199931031265, -0.20266514321065365]
    starting_robot_joints_right = [-1.6545815648737472, -1.6381940802802397, 1.795800360316563, -1.7138684258221923, -1.7362808437379504, -0.01120622072583366]

    # option 1: go straight to the target pose
    # for i in range(20000):
    #     robot_left.servoj(
    #         starting_robot_joints_left, vel=0.001, acc=0.003, t=0.35, lookahead_time=0.2, gain=10, wait=False
    #     )

    # option 2: slowly move to the target pose
    slow_servoj_move(robot_left, starting_robot_joints_left)
    time.sleep(1)
    print('Finished moving the left arm to starting states.')

    # for i in range(20000):
    #     robot_right.servoj(
    #         starting_robot_joints_right, vel=0.01, acc=0.03, t=0.35, lookahead_time=0.2, gain=10, wait=False
    #     )
    slow_servoj_move(robot_right, starting_robot_joints_right)
    time.sleep(1)
    print('Finished moving the right arm to starting states.')
    print('Done')
