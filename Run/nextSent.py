# prevSent.py
# Distant supervision method to check summary in previous sentence to link

import re, spacy, os
from sklearn import metrics
from scipy import stats
import matplotlib.pyplot as plt

# returns boolean value for integer type
def isInt(value) :
	try :
		int(value)
		return True
	except :
		return False

# returns string with URLs replaced with placeholder sentence, 
# list of human-tagged sentences
def returnSpacy(testfile) :
	testsplit = re.split(r"#\d#", testfile)
	tagged = []
	for x in range(0, len(testsplit)) :
		if x % 2 == 1 :
			tagged.append(testsplit[x])

	teststrip = re.sub(r"#\d#", " ", testfile)
	pat = re.escape('-._~:/?#\'[]@!$&()*+,;=%')
	reg = re.compile('\(?(https?://\w*\.?[a-zA-Z0-9]*\.[A-Za-z0-9{}]*)\)?'.format(pat))
	teststrip = re.sub(reg, '. THIS IS ### A URL.', teststrip)
	return teststrip, tagged

# returns list of sentences after URLs
def returnFound(sentences) :
	found = []
	f = []
	for x in range(1, len(sentences)) :
		if re.search("THIS IS ### A URL.", str(sentences[x])) :
			found.append(str(sentences[x + 2]))
	return found

def returnLists(testfile) :
	tagged = []
	t = []
	f = []

	testsplit = re.split(r"#\d#", testfile)

	# tagged sentences
	for x in range(0, len(testsplit)) :
		if x % 2 == 1 :
			tagged.append(testsplit[x])

	teststrip = re.sub(r"#\d#", " ", testfile)
	pat = re.escape('-._~:/?#\'[]@!$&()*+,;=%')
	reg = re.compile('\(?(https?://\w*\.?[a-zA-Z0-9]*\.[A-Za-z0-9{}]*)\)?'.format(pat))
	teststrip = re.sub(reg, '. THIS IS ### A URL.', teststrip)
	nlp = spacy.load('en')
	doc = nlp(teststrip)

	y = 0
	for s in list(doc.sents) :
		if re.search("THIS IS ### A URL.", str(s)) :
			f[len(f) - 1] = 1
		if y < len(tagged) and tagged[y] in str(s) :
			t.append(1)
			y += 1
		else :
			t.append(0)
		f.append(0)

	return t, f

directory = "/Volumes/USB/Research 2017-2018/Run"
p = []
r = []
mi = []
ma = []
pre = 0
rec = 0
fsc = 0
count = 0

for file in os.listdir(directory) :
	if re.match(r"\d+\.txt", file) :
		with open(file, 'r') as test :
			print(file)
			
			testfile = "";

			# Skip until line is an integer
			line = test.readline().strip()
			while isInt(line) == False:
				line = test.readline().strip()
				

			line = test.readline().strip()
			# Add lines until end of text body
			while line != '-------' :
				testfile += (line + " ")
				line = test.readline().strip()


			t, f = returnLists(testfile)
			print(t)
			print(f)
			precision, recall, fscore, support = metrics.precision_recall_fscore_support(f, t)
			# macro = metrics.fbeta_score(f, t, 1, average='macro')
			# micro = metrics.fbeta_score(f, t, 1,average='micro')
			print(precision[1])
			print(recall[1])
			# print(macro)
			# print(micro)
			p.append(precision[1])
			r.append(recall[1])
			# ma.append(macro)
			# mi.append(micro)
			pre += precision[1]
			rec += recall[1]
			fsc += fscore[1]
			count += 1

			# stats.write(file + '\n')
			# stats.write('tagged: ')
			# for item in t :
			# 	stats.write(str(item) + " ")
			# stats.write('\n' + 'found:  ')
			# for item in f :
			# 	stats.write(str(item) + " ")
			# stats.write('\n')

print(str(fsc/count))
# plt.scatter(p, r)
# plt.title('Precision vs. Recall')
# plt.xlabel('Precision')
# plt.ylabel('Recall')
# plt.show()
# plt.scatter(mi, ma)
# plt.title('Micro vs. Macro F-score')
# plt.xlabel('Micro F-score')
# plt.ylabel('Macro F-score')
# plt.show()

# teststrip, tagged = returnSpacy(testfile)
# nlp = spacy.load('en')
# doc = nlp(teststrip)


# sentences = list(doc.sents)
# found = returnFound(sentences)


# print('TAGGED\n')
# for t in tagged :
# 	print(t + '\n')
# print('\nFOUND\n')
# for f in found :
# 	print(f + "\n")
# print("000000000")
# for s in sentences :
# 	print(str(s) + '\n')

