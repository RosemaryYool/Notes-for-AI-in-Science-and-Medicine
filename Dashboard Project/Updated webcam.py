import cv2
import os
import random
import time

def capture_frames():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open webcam")
        return

    # Create folders to save the images
    folder1 = 'folder1'
    folder2 = 'folder2'
    os.makedirs(folder1, exist_ok=True)
    os.makedirs(folder2, exist_ok=True)

    # Capture and save 20 frames with a 1-second interval
    for i in range(20):
        # Capture a single frame
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Generate a random folder number (1 or 2)
        folder_num = random.randint(1, 2)

        # Save the captured frame to the corresponding folder
        if folder_num == 1:
            file_path = os.path.join(folder1, f'frame_{i}.jpg')
        else:
            file_path = os.path.join(folder2, f'frame_{i}.jpg')

        cv2.imwrite(file_path, frame)

        # Display the captured frame
        cv2.imshow('Captured Frame', frame)

        # Wait for 1 second
        time.sleep(1)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the displayed window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_frames()
