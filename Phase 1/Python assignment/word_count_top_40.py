"""printf top 40 most repeated
    words of Tolstoy's story in the
        Top40.txt output file"""

# Imports=====================================================================
from collections import Counter
import re
# Functions defined===========================================================


def remove_punctuation(lines_list):
    """Removes punctuations from a list of lines
        and returns the list of lines"""
    punctuation_free_lines = []
    for line in lines_list:
        line = line.translate({ord(c): "" for c in ',-."_\“”*'})
        line = re.sub("[']", '', line)
        punctuation_free_lines.append(line)
    return punctuation_free_lines
# ----------------------------------------------------------------------------


def get_words(list_of_lines):
    """split lines into list of words
        the words in the list are all made lower case"""
    list_of_words = []
    for line in list_of_lines:
        [list_of_words.append((word.lower()).strip()) for word in line.split()]
    return list_of_words


# Open input files============================================================
with open("2600-0.txt", 'r') as story_file:
    STORY_LINES = [line[:-1] for line in story_file.readlines()]
# ----------------------------------------------------------------------------
with open("stopwords.txt", 'r') as STOP_WORDS:
    STOP_WORDS = [word[:-1] for word in STOP_WORDS.readlines()]
# call functions and stores words===========================================================
WORDS = get_words(remove_punctuation(STORY_LINES))
# Exclude stop words=============================================================
WORDS_WITHOUT_STOP_WORDS = []
for word in WORDS:
    if word not in STOP_WORDS:
        WORDS_WITHOUT_STOP_WORDS.append(word)
WORDS = WORDS_WITHOUT_STOP_WORDS
# Output the results===========================================================
k = 0
for a in WORDS:
    if a == "said":
        k += 1
print(k)
with open("Top40.txt", 'w+') as top_40_words:
    for (word, count) in Counter(WORDS).most_common(40):
        top_40_words.write("{:<9}".format(word) + ": "+str(count)+"\n")
