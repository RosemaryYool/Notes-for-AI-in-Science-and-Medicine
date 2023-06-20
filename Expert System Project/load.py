import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torch.utils.data import TensorDataset, DataLoader
import numpy as np
from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


app = Flask(__name__)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def train():
    data = np.load('dermamnist.npz')
    x = data['train_images']
    y = data['train_labels']

    x_test = data['test_images']
    y_test = data['test_labels']

    y = y[:, 0]
    y_test = y_test[:, 0]

    # Printing the shapes before converting to tensors
    print("Shape of x:", x.shape)
    print("Shape of x_test:", x_test.shape)

    x = np.transpose(x, (0, 3, 2, 1))
    print("Shape of x transposed:", x.shape)

    x_test = np.transpose(x_test, (0, 3, 2, 1))
    print("Shape of x_test transposed:", x_test.shape)

    x = torch.tensor(x).to(device)
    y = torch.tensor(y, dtype=torch.int64).to(device)

    x_test = torch.tensor(x_test).to(device)
    y_test = torch.tensor(y_test, dtype=torch.int64).to(device)

    # Create data loaders
    train_dataset = TensorDataset(x, y)
    test_dataset = TensorDataset(x_test, y_test)

    batch_size = 64

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
            self.relu1 = nn.ReLU()
            self.pool1 = nn.MaxPool2d(2)
            self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
            self.relu2 = nn.ReLU()
            self.pool2 = nn.MaxPool2d(2, padding=1)
            self.fc1 = nn.Linear(32 * 8 * 8, 128)
            self.relu3 = nn.ReLU()
            self.fc2 = nn.Linear(128, 10)

        def forward(self, x):
            print('Input shape inside forward:', x.shape)
            x = x.float() #Convert the input to float
            #x = x.permute(0, 3, 1, 2)
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
    
    model = Net().to(device)

    # Define the loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    num_epochs = 5
    training_loss = []
    
    for epoch in range(num_epochs):
        # Training loop
        model.train()
        epoch_loss = 0
        for images, labels in train_loader:
            optimizer.zero_grad()

            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        epoch_loss /= len(train_loader)
        training_loss.append(epoch_loss)
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}")
    
    print("Training finished!")

    # Plot the training progress
    plt.plot(training_loss)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training Progress")
    plt.savefig('training_plot.png')

    # Test the model
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        accuracy = 100 * correct / total
        print(f"Accuracy of the model on the test images: {accuracy:.2f}%")

# Route for rendering the HTML template
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/display_images')
def display_images():
    data = np.load('dermamnist.npz')
    x = data['train_images']
    y = data['train_labels']

    # Display the first 5 images
    fig, axes = plt.subplots(1, 5)
    for i in range(5):
        axes[i].imshow(x[i])
        axes[i].set_title(f"Label: {y[i]}")
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()

    return "Images displayed successfully"

@app.route('/train', methods=['POST'])
def train_system():
    print("Train system called")
    train()
    training_results = 'Training completed successfully'
    return render_template('index.html', training_results=training_results)


if __name__ == '__main__':
    app.run(debug=True)
