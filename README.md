# Malaria-Detection

**Final Product Hosted On Heroku:** https://malaria-detectorv1.herokuapp.com/

I created a tool that classifies pediatric chest X-rays to detect pneumonia. One way to depict Penumonia is by using chest X-ray images. They are obtain easily but the problem is in radiologic interpretation of images which are not always available. Therefore, such a tool could be use to predict fast and automatically whether or not someone have pneumonia. 

*   Project done using Pytorch Library.
*   I created a tool that classifies pediatric chest X-rays to detect pneumonia.
*   Performed Data preprocessing and Augmentation.
*   Used transfer learning (pretrained resnet34). 
*   Used the learning rate finder to find the best learning rate to update the weights. 
*   Fine-tuned the model.
*   Built a client facing API using Flask.
*   Deployed the model on Heroku.


![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/results%20unfreeze%20pneu.PNG)

## About the Data
Link of the dataset: https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria

**What is Pneumonia:** It is an infection in the lungs tissues caused by microbes. The result is an inflammation which brings water into the lung tissue which can result in breathing problems. "The WHO reports that nearly all cases (95%) of new-onset childhood clinical pneumonia occur in developing countries, particularly in Southeast Asia and Africa. Bacterial and viral pathogens are the two leading causes of pneumonia (Mcluckie, 2009) but require very different forms of management. Bacterial pneumonia requires urgent referral for immediate antibiotic treatment, while viral pneumonia is treated with supportive care. Therefore, accurate and timely diagnosis is imperative." (Quoted from an interesting paper: https://www.cell.com/cell/fulltext/S0092-8674(18)30154-5)

**Medical treatment:** "One key element of diagnosis is radiographic data, since chest X-rays are routinely obtained as standard of care and can help differentiate between different types of pneumonia. However, rapid radiologic interpretation of images is not always available, particularly in the low-resource settings where childhood pneumonia has the highest incidence and highest rates of mortality."(https://www.cell.com/cell/fulltext/S0092-8674(18)30154-5)

**About the Dataset:** The dataset contains 5,863 chest X-Ray images divided into two categories: Pneumonia and Normal.

## Code and Resources Used

**Python Version:** 3.7

**For Web Framework Requirements:** ```pip install -r requirements.txt```

**Fastai Course:** https://github.com/fastai/fastbook


## Chest X-Ray Images Examples

![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/pneumonia%20data.PNG)


## Data Augmentation Strategy
Data Augmentation increases significantly the diversity of images available to train the model. It is a great way to generates new images without collecting new images. These new images are generated from existing ones.
I simply Resized all the images to 460 by 460 pixels. Then I add aug_transforms for each mini-batch: a fastai method to transforms images using the following transformations: mult=1.0, do_flip=True, flip_vert=False, max_rotate=10.0, min_zoom=1.0, max_zoom=1.1, max_lighting=0.2, max_warp=0.2, p_affine=0.75, p_lighting=0.75, xtra_tfms=None, size=224, mode='bilinear', pad_mode='reflection', align_corners=True, batch=False, min_scale=1.0. This technique was introduced in the fastai course 2020, it is called presizing.

![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/data%20aug%20pneumonia.PNG)

## Model Building
* Used transfer learning (pretrained resnet34). Transfer leaning is a method to initialize the weights of a model based on the weights of another model which was already trained. This technique is good to deal with relatively small datasets like this one. In practice we should nearly always use transfer learning.

![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/An-example-of-CNN-architecture.png)
https://www.researchgate.net/figure/An-example-of-CNN-architecture_fig1_320748406

* One of the most important hyperparameter to tune in order to train a model efficiently is the learning rate. If the learning rate is too low, it will take many epochs to train our model, thus the model will be prone to overfitting. If the learning rate is too high,it can cause undesirable divergent behavior. In order to set the appropriate learning rate, I used the learning rate finder from fastai to find the best learning rate to update the weights. 

![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/lr%20finder%20pneu.PNG)

## Model performance
* As we are using transfer learning, I trained the randomly added layers (he head of the model) for 6 epochs, with all other layers frozen (turning requires_grad=False for all the layers of the model except the head: it does not compute the gradients for these layers). Then I unfreezed all of the layers, and trains them all for 4 epochs.

![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/results%20pneu.PNG)

* Then I unfreezed (requries_grad=True) all the layers of the CNN, and trains them all for 4 epochs.

![alt_text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/results%20unfreeze%20pneu.PNG)
![alt text](https://github.com/gaetanlop/Pneumonia-Detection/blob/master/conf%20matrix%20pneu.PNG)

## Productionization and Deployment
I built a client facing API using Voila and deployed it using Heroku.
* **Final Product Hosted On Heroku:** https://pneumonia-detection-appli.herokuapp.com/
