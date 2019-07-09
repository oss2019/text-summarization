# MNIST (Modified National Institute of Standards and Technology database)
- Database of handwritten digits(0-9) that is commonly used for training various image classification tasks.
- Contains 60,000 training images and 10,000 testing images each of 28x28 pixel in grayscale.
- Composed by 500 differenct writers including American Census Bureau employees and American high school students.

## TASK
- The task is to build a classifier which can classify the set of images into 10 different classes(*categories*) one for each digit.
- Understand and build a classifier in **Keras** having an architecture:
  - One hidden layer of size 512
  - Output layer of size 10 (*Number of classes*)
  - For the input layer, stack all the 28x28 pixels of an image into a vector of size 784 (*Can be done using numpy*) and feed into the model.

## PROCESS
### 1. Dataset preprocessing or structuring
Keras has inbuilt mnist dataset. Can be directly imported and used for making train and test datasets.
### 2. Designing the model
  - Keras providies us with two main types of models:
    1. The Sequential Model
    2. Model class with functional API
  - Please find more about the two options from Keras Docs. For this assignment we'll be using sequential model.
  - While adding layers to the sequential model, keras also takes as argument the activation function which you would like to use for each layer. Please find more about the available activation functions from [here](https://keras.io/activations/).  
### 3. Compiling the model
Compile in Keras defines the loss function, the optimizer and the metrics for the model training.
Please find the list of available optimizers in keras from [here](https://keras.io/optimizers/).
### 4. Training the Model
After preparing the dataset and compiling the model, our model now is ready to get trained on the mnist dataset. Keras does all the job of training the model on the dataset using a simple command **fit** which also returns the training history logs.
### 5. Evaluating the model
 Finally, after training the model, we check its performance on the test dataset using the **evaluate** method.
 
 ## CONTRIBUTING
 
 - After completing, send a merge request creating a folder inside the [Keras Assignment](https://github.com/oss2019/text-summarization/tree/master/Framework/Keras/Keras%20Assingment) folder having name as **YourName_Task1**.
 - Inside this folder, place your python script along with the training logs either as an image or as a text file, following the naming conventions **YourName_Model.py** and **YourName_Logs.txt** or **YourName_Logs.jpg** or any supported image type respectively. (Anything more you want to add, just prefix it with **YourName_** inside your folder).
