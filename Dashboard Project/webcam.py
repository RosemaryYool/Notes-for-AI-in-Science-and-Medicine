import cv2
import torch
import numpy as np
from torchvision import transforms


def capture_frame():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open webcam")
        return

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        return

    # Save the captured frame to an image file
    cv2.imwrite('frame.jpg', frame)

    # Convert the frame to RGB (OpenCV uses BGR by default)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the frame to a PyTorch tensor and add a batch dimension
    transform = transforms.ToTensor()
    frame = transform(frame)
    frame = frame.unsqueeze(0)  # Add batch dimension

    # Create a random convolution filter
    conv_filter = torch.randn((3, 3, 3, 3))  # For RGB images

    # Apply the random convolution filter
    filtered_frame = torch.nn.functional.conv2d(frame, conv_filter, padding=1)

    # Convert the filtered frame back to a numpy array and scale it to the range 0-255
    filtered_frame = filtered_frame.squeeze(0)  # Remove batch dimension
    filtered_frame = filtered_frame.permute(1, 2, 0)  # Rearrange dimensions to height x width x channels
    filtered_frame = filtered_frame.detach().numpy()  # Convert to numpy array
    filtered_frame = (filtered_frame - np.min(filtered_frame)) / (np.max(filtered_frame) - np.min(filtered_frame))  # Scale to 0-1
    filtered_frame = (filtered_frame * 255).astype(np.uint8)  # Scale to 0-255

    # Display the filtered frame
    cv2.imshow('Filtered Frame', cv2.cvtColor(filtered_frame, cv2.COLOR_RGB2BGR))  # Convert back to BGR for display

    # Wait for a key press and then close the displayed window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    capture_frame()

