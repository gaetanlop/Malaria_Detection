# Malaria-Detection

## Project Overview

**Final Product Hosted On Heroku:** https://malaria-detectorv1.herokuapp.com/

I created a tool that classifies images of blood cells to detect Malaria. The best way to depict Malaria is by performing a microscopic examination of blood cells. The problem is in the interpretation of these microscopic images.They are not always experts available to interpret them. Therefore, such a tool could be use to predict fast and automatically whether or not someone has Malaria. 

*   Project done using Pytorch Library.
*   I created a tool that classifies images of blood cells to detect Malaria.
*   Performed Data preprocessing and Augmentation.
*   Used transfer learning (pretrained resnet34). 
*   Fine-tuned the model.
*   Built a client facing API using Flask.
*   Deployed the model on Heroku.


![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/images/results%20malaria.PNG)

## Demo

**Final Product Hosted On Heroku:** https://malaria-detectorv1.herokuapp.com/
![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/images/Malaria%20demo.PNG)

## About the Data
Link of the dataset: https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria

**What is Malaria:** "Malaria is a serious and sometimes fatal disease caused by a parasite that commonly infects a certain type of mosquito which feeds on humans. People who get malaria are typically very sick with high fevers, shaking chills, and flu-like illness. Although malaria can be a deadly disease, illness and death from malaria can usually be prevented." (https://www.cdc.gov/malaria/about/index.html#:~:text=Malaria%20is%20a%20serious%20and,%2C%20and%20flu%2Dlike%20illness.)

**Symptoms:** 'Malaria causes symptoms that typically include fever, tiredness, vomiting, and headaches. In severe cases, it can cause yellow skin, seizures, coma, or death. Symptoms usually begin ten to fifteen days after being bitten by an infected mosquito. If not properly treated, people may have recurrences of the disease months later.' (https://en.wikipedia.org/wiki/Malaria)

**About the Dataset:** The dataset contains 27558 images of cells blood divided into two categories: Uninfected and Infected.

## Code and Resources Used

**Python Version:** 3.7

**For Web Framework Requirements:** ```pip install -r requirements.txt```

**Pytorch Documentation:** https://pytorch.org/docs/stable/index.html

**Python Engineer playlist on Pytorch:** https://www.youtube.com/watch?v=EMXfZB8FVUA&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4

## Technical aspects
This project is divided into two part:

* Training a deep learning model using Pytorch. 
  * Steps: 
           
           - Data augmentation
  
           - Data preprocessing: Datasets class, Dataloaders
           
           - Creating the model (using transfer learning). Fine-Tuned the model, Trained all the parameters of the neural net, not only the head of the model
           
           - Creating the training loop: For each batches:predictions/calculate loss/Gradient descent/ update the weights/
           
           - Creating the testing loop: For each batches: predictions, compare with actuals using a particular metric
           
* Building and hosting a Flask web app on Heroku.
  * The user can choose an image from its device.
  * After uploading the image, the user just have to press predict and the prediction will appear

## Malaria images Examples

![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/images/malaria%20data.PNG)

## Data Augmentation Strategy
Data Augmentation increases significantly the diversity of images available to train the model. It is a great way to generates new images without collecting new images. These new images are generated from existing ones.
I decided to use different transforms for the validation set and the training set. 
* For the training set I Resized all the images to 256 by 256 pixels, then centercropped the images to 224 by 224. After that, I applied different transforms: random rotation by 10 degrees, random horizontal and vertical flip with a probability of 50%, then I transformed the Pil Image to a transform, and normalized each channel using Imagenet stats (because I used a pretrained model on Imagenet).
* For the Validation set, I resized the images then centercropped to 224 by 224 pixels. Then transformed the Pil Images to Tensors and Normalized them.

## Model Building
* I used transfer learning (pretrained resnet34). Transfer leaning is a method to initialize the weights of a model based on the weights of another model which was already trained. This technique is good to deal with relatively small datasets like this one. In practice we should nearly always use transfer learning.

![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/images/An-example-of-CNN-architecture.png)
https://www.researchgate.net/figure/An-example-of-CNN-architecture_fig1_320748406


## Model performance
I decided to save my model at each epoch where the validation accuracy increases. I chosed not to save my model when the validation loss decreases following Jeremy Howard advices in his deep learning course. Indeed, validation loss will first get worse during training because the model gets overconfident, and only later will get worse because it is incorrectly memorizing the data. Thus, the most important thing to look at is our metric, here the accuracy.

![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/images/results%20malaria.PNG)
![alt_text](https://github.com/gaetanlop/Malaria_Detection/blob/master/images/classification%20report%20malaria.PNG)
![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/images/confusion%20matrix%20malaria.PNG)
![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/images/graph%20loss%20malaria.PNG)

## Productionization and Deployment
I built a client facing API using Flask and deployed it using Heroku.
* **Final Product Hosted On Heroku:** https://malaria-detectorv1.herokuapp.com/
