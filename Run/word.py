# word.py

import re, spacy, os
from sklearn import metrics
from scipy import stats
import matplotlib.pyplot as plt




directory = "/Volumes/USB/Research 2017-2018/Run"
p = []
r = []
mi = []
ma = []
pre = 0
rec = 0
fsc = 0
count = 0

# for file in os.listdir(directory) :
# 	if re.match(r"\d+\.txt", file) :
# 		# with open(file, 'r') as test :
# 			text = test.read().replace("\n\n", "###NEW###")

# 			textedit = re.split(r"\d+###NEW###", text)
# 			text = textedit[1]
# 			print(text)

# 			textedit = re.split('-------', text)
# 			text = 

# 			nlp = spacy.load('en')

fsc = 0
count = 0
for file in os.listdir(directory) :
	if re.match(r"\d+\.txt", file) :
		with open(file, 'r') as test :
			text = test.read().replace("\n\n", " ###NEW### ")

			textedit = re.split(r"###NEW### \d+ ###NEW###", text)
			text = textedit[1]

			textedit = re.split('-------', text)
			text = textedit[0]

			# print(text)

			testsplit = re.split(r"#\d#", text)
			tagged = []
			for x in range(0, len(testsplit)) :
				if x % 2 == 1 :
					tagged.append(testsplit[x])


			teststrip = re.sub(r"#\d#", " ", text)
			pat = re.escape('-._~:/?#\'[]@!$&()*+,;=%')
			reg = re.compile('\(?(https?://\w*\.?[a-zA-Z0-9]*\.[A-Za-z0-9{}]*)\)?'.format(pat))
			teststrip = re.sub(reg, '. THIS IS ### A URL.', teststrip)

			nlp = spacy.load('en')
			doc = nlp(teststrip)

			y = 0


			t = []
			f = []
			for s in list(doc.sents) :
				if re.search("jsyk", str(s).lower()) :
					f.append(1)
				else :
					f.append(0)
				if y < len(tagged) and tagged[y] in str(s) :
					t.append(1)
					y += 1
				else :
					t.append(0)

				# print(str(s) + "\n")

			# f.append(0)
			# print(teststrip)
			print(str(file))
			print(t)
			print(f)
			precision, recall, fscore, support = metrics.precision_recall_fscore_support(f, t)
			print(precision[1])
			print(recall[1])
			fsc += fscore[1]
			count += 1


print(str(fsc/count))
