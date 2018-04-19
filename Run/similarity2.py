# similarity2.py
from __future__ import unicode_literals
import re, spacy, os, glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy import stats



def isInt(value) :
	try :
		int(value)
		return True
	except :
		return False


directory = "/Volumes/USB/Research 2017-2018/RunNew"

alltext = ""

vectorizer = TfidfVectorizer()

nlp = spacy.load('en')


# for file in os.listdir(directory) :
# 	with open(os.path.join(directory, file), "r") as text :
# 		alltext += text.read()

total = open(os.path.join(directory, "total.txt"), 'r')
alltext = total.read()
doc = nlp(alltext.decode('utf-8'))
print(alltext)
# print(list(doc.sents))
allfit = vectorizer.fit([sent.string.strip() for sent in doc])
total.close()



results = []
for file in os.listdir(directory) :
	with open(os.path.join(directory, file), 'r') as text :
		if (file != "total.txt") :
			doc = nlp(text.read().decode('utf-8'))
			results.append(vectorizer.transform(sent.string.strip() for sent in doc))


results1 = []
for x in range(0, len(results)) :
	results1.append(cosine_similarity(results[0], results[x]))

print(results1)
