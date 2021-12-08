# Exotic-Fruit-Recognition
## Summary
Nowadays in supermarkets you see variety of fruits, and also a seperate section for exotic fruits. Many questions pop up in mind as you glance them. For eg:
  1. What is the name?
  2. Where is it from?
  3. How it tastes and about its texture and so on....

Keeping this in mind a Exotic fruit recognition model is created which takes the image of the fruit and predicts whether it is a exotic fruit or not. To start with 4 types of exotic fruits have been chosen and they are Kaki, Cherimoya, Rambutan and Mangosteen. The tools used are Tensorflow, Keras and google colab.

## Collecting Data
Data is been collected by downloading the images from Flickr using api's and then labelling them. The images are then pre processed accorcing to the model requirements. Due to scarcity of images to run the model Data Augmention is done.

## Model
A Neural Network model is built along with a Pre-trained convolutional neural network named VGG16 obtained from keras applications which is trained on a dataset of over 15 million labeled high-resolution images belonging to different categories. Note that the trained model must not be trained once again. By using the weights of the trained model, the newly built model is trained with the train dataset. The accuracy of the model is evaluated and predictions are made. 

## Conclusion
As the test accuracy of the model not more than 95%, it can be improved by fine tuning the hyperparameters. To deploy the model as a web app is in progress.
Futher changes can be done by adding more number of exoic fruit classes and also a short description of the fruit like its origin, nutritional values, how it can be used in various cuisines.


