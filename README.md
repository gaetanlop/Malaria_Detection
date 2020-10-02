# Malaria-Detection

## Project Overview

**Final Product Hosted On Heroku:** https://malaria-detectorv1.herokuapp.com/

I created a tool that classifies images of blood cells to detect Malaria. The best way to depict Penumonia is by performing a microscopic examination of blood cells. The problem is in the interpretation of these microscopic images.They are not always experts available to interpret them. Therefore, such a tool could be use to predict fast and automatically whether or not someone has Malaria. 

*   Project done using Pytorch Library.
*   I created a tool that classifies images of blood cells to detect Malaria.
*   Performed Data preprocessing and Augmentation.
*   Used transfer learning (pretrained resnet34). 
*   Fine-tuned the model.
*   Built a client facing API using Flask.
*   Deployed the model on Heroku.


![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/results%20malaria.PNG)

## Demo

**Final Product Hosted On Heroku:** https://malaria-detectorv1.herokuapp.com/
![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/Malaria%20demo.PNG)

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

## Malaria images Examples

![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/malaria%20data.PNG)

## Data Augmentation Strategy
Data Augmentation increases significantly the diversity of images available to train the model. It is a great way to generates new images without collecting new images. These new images are generated from existing ones.
I simply Resized all the images to 460 by 460 pixels. Then I add aug_transforms for each mini-batch: a fastai method to transforms images using the following transformations: mult=1.0, do_flip=True, flip_vert=False, max_rotate=10.0, min_zoom=1.0, max_zoom=1.1, max_lighting=0.2, max_warp=0.2, p_affine=0.75, p_lighting=0.75, xtra_tfms=None, size=224, mode='bilinear', pad_mode='reflection', align_corners=True, batch=False, min_scale=1.0. This technique was introduced in the fastai course 2020, it is called presizing.

## Model Building
* Used transfer learning (pretrained resnet34). Transfer leaning is a method to initialize the weights of a model based on the weights of another model which was already trained. This technique is good to deal with relatively small datasets like this one. In practice we should nearly always use transfer learning.

![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/An-example-of-CNN-architecture.png)
https://www.researchgate.net/figure/An-example-of-CNN-architecture_fig1_320748406



## Model performance


![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/results%20malaria.PNG)
![alt_text](https://github.com/gaetanlop/Malaria_Detection/blob/master/classification%20report%20malaria.PNG)
![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/confusion%20matrix%20malaria.PNG)
![alt text](https://github.com/gaetanlop/Malaria_Detection/blob/master/graph%20loss%20malaria.PNG)

## Productionization and Deployment
I built a client facing API using Voila and deployed it using Heroku.
* **Final Product Hosted On Heroku:** https://malaria-detectorv1.herokuapp.com/
