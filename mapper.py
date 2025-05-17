#!/usr/bin/env python
import sys
#import nltk
#nltk.download('stopwords')
#from nltk.corpus import stopwords

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words; splits on any whitespace
    words = line.split()
    #stopwords = ('the', 'and', 'to', 'of', 'you', 'a', 'an', 'I', '.', '!')
    #stopwords = stopwords + (',', ';', 'my', ':', '?', 'in', 'is', 'not', 'that', 'me', 'And', 'it')
    # output tuples (word, 1) in tab-delimited format
    #stopwords_array = stopwords.words('english')
    file_path = 'nltk_stop_words.txt'
    stopwords = ['.', ',', '!', '?', ':', ';']
    with open(file_path, 'r') as file:
        stopword_lines = file.readlines()
        #print(stopword_lines)
        for stopword_line in stopword_lines:
            stopwords.append(stopword_line.strip())
    #print(stopwords)
    #with open(file_path, 'w') as file:
    #    for word in stopwords_array:
    #        file.write(word + '\n')
    for word in words:
        if word not in stopwords:
            print(word + '\t1')
