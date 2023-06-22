from flask import Flask, render_template, request, Response
import cv2
import torch
import numpy as np
from torchvision import transforms
import time
import os

app = Flask(__name__)
Response.default_content_type = 'text/html'

num_images_captured = 0

# Get the path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the directory path where you want to save the images
image_dir = os.path.join(current_dir, 'images')

# Create the "images" directory if it doesn't exist
if not os.path.exists(image_dir):
    os.makedirs(image_dir)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture_frame():
    global num_images_captured
    
    msg = 'Image captured and processed successfully'
    
    cap = cv2.VideoCapture(0)

    
    while num_images_captured < 10:
        if not cap.isOpened():
            msg = "Cannot open webcam"
            break
	    
        # Capture a single frame
        ret, frame = cap.read()

        if not ret:
            msg = "Can't receive frame (stream end?). Exiting ..."
            break


        # Save the captured frames to an image file
        cv2.imwrite(os.path.join(image_dir, 'frame{}.jpg'.format(num_images_captured)), frame)


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

        num_images_captured += 1
        
        # Delay before closing the displayed window
        time.sleep(1)
    
    
        # Check if the desired number of images is captured
        if num_images_captured >= 10:
            # Perform any necessary cleanup or further processing
            # Once the desired number of images is captured
            break
    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()
    # Return a response if needed
    return msg

if __name__ == "__main__":
    app.run(debug=True, port=8011)

