import urx
import time

def slow_servoj_move(robot, q_target, steps=300):
    q_current = robot.getj()
    
    for i in range(steps):
        q_interp = [(1 - i/steps) * q_current[j] + (i/steps) * q_target[j] for j in range(6)]
        try:
            robot.servoj(q_interp, vel=0.001, acc=0.003, t=0.3, lookahead_time=0.2, gain=300, wait=False)
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

    # option 1: starting states for our robots in GELLO and real-world experiments (two arms facing each other https://www.dropbox.com/scl/fi/sd7q4cc3jhuwolip1q4ur/2025_03_10_gello_setup.jpg?rlkey=0b7l4rnyz6oq2t34z5m09nmxp&dl=0)
    # joint angles: 0, -60, -120, -90, 90, 80
    starting_robot_joints_left = [0.03562357192119225, -1.0166193892985, -2.1039916031110013, -1.6265433936482632, 1.6158471255263718, 1.4326387187095664]
    # joint angles: 0, -120, 120, -90, -90, 80
    starting_robot_joints_right = [-0.13006933731761716, -2.161462890219333, 2.1741989572528118, -1.6085602612338965, -1.6198960915012304, 1.41713373225814]
    
    # option 2: starting states for our robots in GELLO and real-world experiments (two arms facing the wall)
    # starting_robot_joints_left = [1.3780459778509433, -1.523749890442781, -1.5899893346228173, -1.523211104456275, 1.722199931031265, -0.20266514321065365]
    # starting_robot_joints_right = [-1.6545815648737472, -1.6381940802802397, 1.795800360316563, -1.7138684258221923, -1.7362808437379504, -0.01120622072583366]

    # slowly move to the target pose
    slow_servoj_move(robot_left, starting_robot_joints_left)
    time.sleep(1)
    print('Finished moving the left arm to starting states.')

    slow_servoj_move(robot_right, starting_robot_joints_right)
    time.sleep(1)
    print('Finished moving the right arm to starting states.')
    print('Done')
