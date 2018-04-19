# similarity.py

import re, spacy, os
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from scipy import stats


def isInt(value) :
	try :
		int(value)
		return True
	except :
		return False


with open('0.txt', 'r') as test :

	filename = '0'

	# # Skip until number
	# print(test.read())
	# line = test.readline().strip()
	# # print(line)
	# while isInt(line) == False :
	# 	line = test.readline().strip()
	# count = int(line)

	# line = test.readline().strip()
	# while line != '_______' :
	# 	# print(line)
	# 	post += (line + " ")
	# 	line = test.readline().strip()

	# articles = []

	# for x in range(0, count) :
	# 	a = ""
	# 	line = test.readline().strip()
	# 	while line != '_______' :
	# 		a += (line + " ")
	# 	articles.append(a)

	# print(articles)



	text = test.read()
	textedit = re.split(r"\n\n\d+\n\n", text)
	text = textedit[1]


	text = re.split("-------", text)


	nlp = spacy.load('en')



	with open(filename + "_post.txt", 'r+') as current :
		current.write(text[0])
		vectorizer = TfidfVectorizer()
		print(vectorizer.fit_transform(current.readlines()))
	


	count = 1
	articles = []
	results = []
	for x in range (1, len(text) - 1) :
		with open(filename + "_" + str(count) + ".txt", 'r+')  as current :
			current.write(text[x])
			print(vectorizer.fit_transform(current.readlines()))
			count += 1




	# results = []

	# for s in list(textparsed[0].sents) :
	# 	print(str(s))

