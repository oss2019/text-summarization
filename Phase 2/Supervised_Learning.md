# The Supervised Learning Paradigm

Supervision in machine learning, or supervised learning, refers to cases where the ground truth for the
targets (what’s being predicted) is available for the observations. For example, in document
classification, the target is a categorical label, and the observation is a document. In machine
translation, the observation is a sentence in one language and the target is a sentence in another
language.And similarly in text summarization, the observation is any text input and the target is much simplified and shorter text. With this understanding of the input data, the figure below illustrates the supervised learning paradigm:




![supervised learning](https://github.com/Sedherthe/text-summarization/blob/master/Phase%202/images/supervised_learning.png)



We can break down the supervised learning paradigm, as illustrated in the Figure, to six main concepts:

* **Observations**

  Observations are items about which we want to predict something. We denote observations using
  x. We sometimes refer to the observations as inputs.
  
* **Targets** 
  
  Targets are labels corresponding to an observation. These are usually the things being predicted.
  Following standard notations in machine learning/deep learning, we use y to refer to these.
  Sometimes, these labels known as the ground truth.
  
* **Model**
  
  A model is a mathematical expression or a function that takes an observation, x, and predicts the
  value of its target label.
  
* **Parameters**
  
  Sometimes also called weights, these parameterize the model. It is standard to use the notation w
  (for weights) or ŵ.
  
* **Predictions**
  
  Predictions, also called estimates, are the values of the targets guessed by the model, given the
  observations. We denote these using a “hat” notation. So, the prediction of a target y is denoted as
  ŷ.
  
* **Loss Function**
  
  A loss function is a function that compares how far off a prediction is from its target for
  observations in the training data. Given a target and its prediction, the loss function assigns a scalar
  real value called the loss. The lower the value of the loss, the better the model is at predicting the
  target. We use L to denote the loss function.
  
  
