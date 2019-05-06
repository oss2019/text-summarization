# Python Word Count

You've likely seen word-clouds before, if not, please check [here](https://www.google.com/search?site=&tbm=isch&source=hp&biw=1536&bih=799&q=word+cloud&oq=word+cloud&gs_l=img.3..0l10.981.2160.0.2280.11.11.0.0.0.0.95.704.9.9.0....0...1.1.64.img..2.9.695.0.NtfMDYloQTw) for examples. In order to create word clouds, the software finds the most frequently occurring words in a text file. This assignment will ask you to do just that! We'll use the text of the famous novel by Leo Tolstoy, **War and Peace** for this assignment!!

## Part 1 : Writing and running Python code

Make sure you have the environment for coding already setup. Feel free to create a python program using a text editor or you can do all the work in python shell.  Or, if you already have some experience in Jupyter notebooks, feel free to do your work there instead.
If you have any doubts, feel free to ping us any time or just open an issue if you feel so .. 

## Part 2 : Grab the source files

Get the resources for this assignment [here](https://github.com/oss2019/text-summarization/tree/master/Phase%201/Python%20assignment/resources)!

1. 2600-0.txt : War and Peace - Leo Tolstoy. Credit to [Project Gutenberg](https://www.gutenberg.org/)
2. stopwords.txt : common words to exlude. Credit to [Andreas Mueller](https://github.com/amueller/word_cloud/)

## Part 3 : Word Count

To complete this assignment, you will want to read and clean the input, then count the frequencies of each word. Remember that the data pre processing step is the most important step for any analysis which you do! Go through the dataset(text file here) atleast once and then go on with your analysis!

Your overall approach should be : 
- Think of a data structure to store the words and the number of occurrances of the word.
- Read in each word from the file, **making it lower case and removing punctuation**. ( Remove the punctuation marks from the file).
- For simplicity and to keep the results uniform consider **only the following **10** punctuation marks for removal:**   
  **( ",", "-", "'", ".", '"', '_', '\\', '“', '”', '*')**
- Then extract the **Top x** positions which you would like from any one of the issues.!!
- Also don't forget to **exclude the stopwords**(common words).
- If you used an unordered data structure like a dictionary, you might need to get the values out of it (into a list) to sort it.  You could also use [collections.Counter](https://docs.python.org/2/library/collections.html) from the Collections module to help with this step!
- Please note the output format for your file :-
  
  **word1 : number_of_occurrences**
  
  **word2 : number_of_occurrences**
  
- We have opened an issue for every **Top x most common words**; So everyone can work on any one of these issues.
- Finally create a file named **Topx.txt** for your issue and place it in the the Python assignment folder inside Phase 1 directory.
As an example, if you are working on the issue **Top 15 most common words**, then place the file **Top15.txt** inside **Phase 1/Python assignment/**

- Also feel free to verify other contributors most occurring words with yours and in case of mismatch you can point out on their issue if you're confident that your's right!*(Maybe extra points for this :p)*
- Using the given stopwords and removing the above 10 punctuation marks here are the **Top 3 most common words** which we found :
  
  **said : 2762**
  
  **one : 2008**
  
  **prince : 1856**
