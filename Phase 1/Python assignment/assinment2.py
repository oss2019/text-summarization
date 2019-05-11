import numpy
import sys
from itertools import izip


def replace_new(punctuations,all_words):
	new_words = []
	new_words = all_words
	for i in punctuations:
		count = 0
		for j in new_words:
			if i == j:
				count +=1
		new_words = new_words.replace(str(i),' ',count)
	return new_words

def remove_new(stopwords,all_words):
	new_words = []
	new_words = all_words
	for i in stopwords:
		count = 0
		for j in new_words:
			if i == j:
				count +=1
		for k in range(0,count):
			new_words.remove(str(i))
	return new_words





#with open("stopwords.txt" , "r").read().split('\n') as file1
#with open("warandpeace.txt" , "r").read().split() as file2

file1 = open("stopwords.txt" , "r").read().split('\n')

stopwords = []

for i in file1:
	stopwords.append(i)

stopwords.pop(-1)
#print stopwords

punctuations = "`~!@#$%^&*()_+-={}[]:;'<,>.?/|"
newline_punctuations = '\n'
newline_punctuations1 = '"'


file2 = open("warandpeace.txt" , "r")

all_words = []

all_words = str(file2.read())
#print(all_words)

all_words=all_words.lower()

all_words = replace_new(punctuations,all_words)
all_words = replace_new(newline_punctuations,all_words)
all_words = replace_new(newline_punctuations1,all_words)

#print(all_words)
all_words_copy = all_words #to be removed

all_words = all_words.split(' ')
#print(all_words)


all_words = remove_new(stopwords,all_words)
	
#all_words = all_words.split(' ')	
#print(all_words)

words_frequency = {}

for i in all_words:
	counter = 24
	for k in words_frequency:
		if i == k:
			counter = counter * 0
		else:
			counter = counter * 1
	if counter:
		frequency = 0
		for l in all_words:
			if i == l:
				frequency = frequency + 1
			else:	
				frequency = frequency + 0
		if frequency > 1500 :
			words_frequency[frequency] = i
			print(words_frequency)





""""
all_words = []

counter = 5

frequency = 0

for i in file2:
	j = i.lower()
	all_words.append(j)
#print(all_words)
print(len(all_words))

words_frequency = {}

#for i in stopwords:
#	all_words.remove(i)
#print(len(all_words))

for i in all_words:
	counter = 24
	for j in stopwords:
		if i == j :
			counter = counter * 0
		else:
			counter = counter * 1
	for k in words_frequency:
		if i == k:
			counter = counter * 0
		else:
			counter = counter * 1
	if counter:
		frequency = 0
		for l in all_words:
			if i == l:
				frequency = frequency + 1
			else:	
				frequency = frequency + 0
		if frequency > 700 :
			words_frequency[frequency] = i
			print(words_frequency)

print('\n\n\n Here is :\n')
print(words_frequency)






"""
"""
for i in all_words:
	for j in stopwords:
		if i==j:
			count = count*0
		else:
			count = count*1
	if count != 0:
		frequncy = 0		
		for k in all_words:
			if i==k:
				frequency += 1
	words_frequency[frequency] = i

#print(words_frequency)


"""
