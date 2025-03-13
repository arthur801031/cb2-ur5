import pyrealsense2 as rs
import numpy as np
import cv2

# Reset the camera before starting
ctx = rs.context()
devices = ctx.query_devices()
for dev in devices:
    dev.hardware_reset()

# Initialize Intel RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()

# Enable depth stream at VGA resolution (640x480) with 30 FPS
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start streaming
pipeline.start(config)

def show_depth(event, x, y, flags, param):
    """ Display depth at the clicked pixel """
    if event == cv2.EVENT_LBUTTONDOWN:
        depth_value = param[y, x]  # Get depth in millimeters
        print(f"Depth at ({x}, {y}): {depth_value} mm")

# Create OpenCV window
cv2.namedWindow('Depth Stream', cv2.WINDOW_AUTOSIZE)

while True:
    # Capture frames
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    
    if not depth_frame:
        continue
    
    # Convert depth frame to numpy array
    depth_image = np.asanyarray(depth_frame.get_data())
    
    # Normalize depth image for better visualization
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

    # Display depth image
    cv2.imshow('Depth Stream', depth_colormap)
    
    # Set mouse callback for depth value display
    cv2.setMouseCallback('Depth Stream', show_depth, depth_image)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Clean up
cv2.destroyAllWindows()
pipeline.stop()