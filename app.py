import io
import torch 
import torch.nn as nn 
from torchvision import transforms,models

from PIL import Image

from flask import Flask, redirect, url_for, request, render_template



# Define a flask app
app = Flask(__name__)


class_names=['Parasitized','Uninfected']
device = torch.device('cpu')
model=models.resnet34(pretrained=True)
model.fc = nn.Linear(512, 2)

model.load_state_dict(torch.load('model.pt', map_location=device))
model.eval()

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(256),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize([0.485, 0.456, 0.406], 
                                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model(tensor)
    _, y_hat = torch.max(outputs,1)
    predicted_idx = y_hat.item()
    return class_names[predicted_idx]
    
@app.route('/')
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        file = request.files['file']

        # Save the file to ./uploads
        
        
        img_bytes = file.read()
        #make predictions
        class_name = get_prediction(image_bytes=img_bytes)
        return class_name
    return None


if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
