Task for data manipulation-
We will now begin the process of text summarization-
So first things first, the dataset. Since this is our first trial we will be using the amazon fine food reviews dataset to perform our summarization task
You can find our implementation of the code in the repo
https://github.com/ganeshsamarth/text_summarization_test.git

Please find the dataset in the below mentioned link which has been hosted on kaggle.
https://www.kaggle.com/snap/amazon-fine-food-reviews

This will download the csv file on to your local machine.
You will be using pandas to import this csv file into your python script.

The first step to text summarization is dataset manipulation. We will be doing the following steps to make our data ready so as to feed it as input to our network. You might also want to use the regex library to work with your data.
Here are the steps you will have to perform-
1. Open a python interpreter on your virtual environment and add the following command to download the stopwords in english from the nltk library.

import nltk
nltk.download('stopwords')

2.Now we begin the actual  scripting-
First import the csv file and run these commands-
data=pd.read_csv("/home/pbu/Downloads/amazon-fine-food-reviews/Reviews.csv",nrows=100000)
data.drop_duplicates(subset=['Text'],inplace=True)#dropping duplicates
data.dropna(axis=0,inplace=True)#dropping na

3. Convert the text to lower case.
4. Use BeautifulSoup to append the article into one string using the lxml parser
5. Remove all punctuation marks i.e \([^)]*\)
6.Replace all contraction mappings with their longer forms (See reference i.e. the repo)
7. We want only letters in our dataset as of now, so we need to remove everything that is not in a-z. Try the negative character set.
7. Remove stopwords only for the main text and not the summary
8. Remove all short words (i.e words with length lesser than three).

Take into consideration reviews and summaries which have the maximum word count to be 30 and 8 respectively.

Add a start token and an end token to each of the summaries.
Make sure the data is in the form of a dictionary.
Print 3 examples each of reviews and summaries as the final output of your code.



This ends the first part of the text summarization-the preprocesing.

Next steps-
Implement keras tokenizer
Build the network
Train the network
Watch the magic!



