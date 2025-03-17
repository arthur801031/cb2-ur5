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
    # starting_robot_joints_left = [0.03562357192119225, -1.0166193892985, -2.1039916031110013, -1.6265433936482632, 1.6158471255263718, 1.4326387187095664]
    # joint angles: 0, -120, 120, -90, -90, 80
    # starting_robot_joints_right = [-0.13006933731761716, -2.161462890219333, 2.1741989572528118, -1.6085602612338965, -1.6198960915012304, 1.41713373225814]
    
    # option 2: starting states for our robots in GELLO and real-world experiments (two arms facing the wall https://www.dropbox.com/scl/fi/p5ynkage2bhs5y3lcqq5r/2025_corl_real_world_setup3.jpg?rlkey=rl5qaph1nomwznj58855d0cvc&dl=0)
    # joint angles: 80, -65, -115, -93, 100, 159
    starting_robot_joints_left = [1.3629151365049208, -1.1219412063110294, -2.036740639010723, -1.632770313019793, 1.7637373624131287, 2.771111558000195]
    # joint angles: -80, -115, 118, -90, -92, 0
    starting_robot_joints_right = [-1.4106484960522758, -1.9944810024925443, 2.054192150410259, -1.5718085742732786, -1.6140418455715997, 0.061382133371988376]

    # slowly move to the target pose
    print('Moving the left arm....')
    slow_servoj_move(robot_left, starting_robot_joints_left)
    time.sleep(1)
    print('Finished moving the left arm to starting states.')

    print('Moving the right arm....')
    slow_servoj_move(robot_right, starting_robot_joints_right)
    time.sleep(1)
    print('Finished moving the right arm to starting states.')
    print('Done')
