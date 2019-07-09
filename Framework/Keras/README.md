# Text Summarization-Python Keras

Hey Everyone! So we ran our test about right and here we show you a glimpse of how text summarization using deep learning is going to be like.
We used a basic seq2seq model and a pretty concise dataset to generate our summmaries, it might not be as great as human level but it sure works!

After training on the amazon reviews dataset,
Here goes---
## Review #1
These are sooooo good! Addictive. Just know they're not CARROT chips/fries (actual fried carrot slices) they're carrot CHIPS - think POTATO chips (actual fried potato) vs corn CHIPS (cornmeal fried chip, basically). Trying to use inflection for emphasis there. Either you love or hate but my entire family craves these!

### Original Summary #1
Love These!

### Generated Summary #1
love these chips 

Cool right! The model is able to recognize the fact that the main topic of discussion in the entire review was about chips.
This model is still in its basic stages and lots of improvements can be built upon this. 

This deep learning model was built in a framework known as keras with tensorflow backend. Now for all those who have done the courses of Deep Learning would  have definetely heard of these names.

Before we dive into the text summarization we wanted to give you a decent idea of how to work with these frameworks

Please follow these instructions carefully:(You need to get this right)
- We will be mainly focuing on Linux based OS. 
- Since we do not want to disrupt various versions of various python packages in your system, we would be running all your scripts on a python virtual environment. (its also considered good practice!)
- For all those who do not know what is a python virtual environment and how to work on it, well virtual environment as the name suggests is like a virtual world where you can install  particular versions of all your dependecies for a project without actually changing your system configurations.
- This also makes sure that none of you will run into version troubles while executing your scripts.
- To install and use python virtual environment, just have a look at this [link](
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
- Please do create a virtual environment with **python3**.Also, after creating your venv please verify your python version using the command:
`python --version`

- Once you have activated your virtual environment, to get working with Keras install the following:
  - pip install bs4
  - pip install matplotlib
  - pip install h5py
  - pip install sklearn
  - pip install numpy
  - pip install tensorflow==1.14.0
  - pip install keras==2.2.4
  - pip install pandas
  - pip install nltk
  - pip install lxml
