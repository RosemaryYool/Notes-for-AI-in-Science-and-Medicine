import cv2
import os
from datetime import datetime

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Global variable to track motion detection
motion_detected = False

def capture_motion():
    global motion_detected

    # Check if motion was detected
    if motion_detected:
        # Capture a single frame
        ret, frame = cap.read()

        # If the frame was successfully captured
        if ret:
            # Generate a unique filename based on the current timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = f'motion_{timestamp}.jpg'

            # Save the image
            cv2.imwrite(image_path, frame)
            print(f"Motion detected! Image saved as {image_path}")

            # Reset motion detection flag
            motion_detected = False

def motion_detection():
    global motion_detected

    # Set up motion detection parameters
    motion_threshold = 1000

    # Read the first frame for motion detection
    _, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

    while True:
        # Read the current frame
        ret, frame = cap.read()

        # If the frame was successfully captured
        if ret:
            # Convert the frame to grayscale and apply Gaussian blur
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            # Calculate the absolute difference between the current and previous frames
            frame_diff = cv2.absdiff(prev_gray, gray)

            # Apply thresholding to highlight the differences
            _, threshold = cv2.threshold(frame_diff, 20, 255, cv2.THRESH_BINARY)

            # Calculate the total number of non-zero pixels in the threshold image
            motion_pixels = cv2.countNonZero(threshold)

            # If the number of motion pixels exceeds the threshold, set motion_detected flag to True
            if motion_pixels > motion_threshold:
                motion_detected = True

            # Update the previous frame for the next iteration
            prev_gray = gray

        # Call capture_motion function if motion is detected
        capture_motion()

        # Wait for a key press and exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Start the motion detection
    motion_detection()
