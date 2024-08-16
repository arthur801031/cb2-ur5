Control UR5 using `urx`. More examples: https://github.com/SintefManufacturing/python-urx.
* We use a local version of `urx` because there's formatting issue with `tpose`.

**`test_robotiq_gripper.py`**

- Activate and control the Robotiq gripper. Note that every time you start a program you need to activate the gripper to use it.

**`opencv_viewer_example.py`**

- Stream Intel RealSense camera.

**`get_robot_tool_tip_pos.py`**

- Get robot’s tool tip position (x, y, z) in robot base frame.

**`get_set_two_robot_joints.py`**

- Move the robot arms to pre-configured poses. I use this code to move the robot arms to the starting states before my experiments.

**`verify_camera_calibration.py`**

- I use this code to test my camera calibration result. Specifically, it captures RGB-D images from the RealSense camera and display point cloud in Open3D. Then, I select a point in the viewer, and the robot arm would move its end-effector to that position.

**`servoj_example.py`**

- Example code that moves the robot arm using joint-space control.
