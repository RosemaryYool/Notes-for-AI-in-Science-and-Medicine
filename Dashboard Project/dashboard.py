from flask import Flask, render_template, request, Response
import cv2
import torch
import numpy as np
from torchvision import transforms
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import time
import os
import random
import matplotlib.pyplot as plt

app = Flask(__name__)
Response.default_content_type = 'text/html'

num_images_captured = 0

# Get the path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the directory paths where you want to save the images
folder1 = os.path.join(current_dir, 'folder1')
folder2 = os.path.join(current_dir, 'folder2')

# Create the folders if they don't exist
os.makedirs(folder1, exist_ok=True)
os.makedirs(folder2, exist_ok=True)

# CNN Model Training

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2, padding=1)
        self.fc1 = nn.Linear(32 * 57 * 57, 128)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(128, 2)  # 2 output classes


    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.relu3(x)
        x = self.fc2(x)
        return x
    
# Create an instance of the CNN model
model = CNN()

# Define the loss function
loss_function = nn.CrossEntropyLoss()

# Define the optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Move the model to the device (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Load and preprocess the images from folders
def load_images_from_folder(folder):
    images = []
    labels = []

    for filename in os.listdir(folder):
        if filename.endswith('.jpg'):
            image_path = os.path.join(folder, filename)
            image = cv2.imread(image_path)
            resized_image = cv2.resize(image, (224, 224))
            rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
            images.append(rgb_image)
            labels.append(0 if folder == folder1 else 1)

    images = np.array(images)
    labels = np.array(labels)

    preprocessed_images = torch.from_numpy(images).permute(0, 3, 1, 2).float()
    return preprocessed_images, labels

# Load images from folder1
folder1_images, folder1_labels = load_images_from_folder(folder1)

# Load images from folder2
folder2_images, folder2_labels = load_images_from_folder(folder2)

# Combine the images and labels from both folders
all_images = torch.cat((folder1_images, folder2_images))
all_labels = np.concatenate((folder1_labels, folder2_labels))

# Create the TensorDataset
dataset = TensorDataset(all_images, torch.from_numpy(all_labels))

# Define the batch size and create the DataLoader
batch_size = 1
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Training Loop
num_epochs = 15
losses = []  # List to store the losses for plotting

for epoch in range(num_epochs):
    epoch_loss = 0.0  # Variable to store the loss for the current epoch
    for images, labels in data_loader:
        # Move the images and labels to the device
        images = images.to(device)
        labels = labels.to(device)

        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(images)

        # Calculate the loss
        loss = loss_function(outputs, labels)

        # Backward pass
        loss.backward()

        # Update the weights
        optimizer.step()

        epoch_loss += loss.item()

    epoch_loss /= len(data_loader)  # Calculate average loss for the epoch
    losses.append(epoch_loss)  # Store the loss for plotting

    print(f"Epoch: {epoch+1}/{num_epochs}, Loss: {epoch_loss:.4f}")

# Plot the training progress
plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Progress')
plt.show()

@app.route('/')
def serve_html():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture_frames():
    global num_images_captured

    msg = 'Image capture and processing complete'

    cap = cv2.VideoCapture(0)

    while num_images_captured < 20:
        if not cap.isOpened():
            msg = "Cannot open webcam"
            break

        # Capture a single frame
        ret, frame = cap.read()

        if not ret:
            msg = "Can't receive frame (stream end?). Exiting ..."
            break

        # Generate a random folder number (1 or 2)
        folder_num = random.randint(1, 2)

        # Save the captured frame to the corresponding folder
        if folder_num == 1:
            file_path = os.path.join(folder1, f'frame_{num_images_captured}.jpg')
        else:
            file_path = os.path.join(folder2, f'frame_{num_images_captured}.jpg')

        cv2.imwrite(file_path, frame)

        num_images_captured += 1

        # Pause for a short time before capturing the next frame
        time.sleep(0.1)

    cap.release()
    cv2.destroyAllWindows()

    return msg


if __name__ == '__main__':
    app.run(debug=True, port=8011)

