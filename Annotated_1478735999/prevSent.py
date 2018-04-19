# prevSent.py
# Distant supervision method to check summary in previous sentence to link

import re, spacy, os

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

# returns list of sentences before URLs
def returnFound(sentences) :
	found = []
	f = []
	for x in range(1, len(sentences)) :
		if re.search("THIS IS ### A URL.", str(sentences[x])) :
			found.append(str(sentences[x - 1]))
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

directory = os.fsencode("/Volumes/USB/Research 2017-2018/Annotated_1478735999")
print('hi')
for file in os.listdir(directory) :
	filename = os.fsdecode(file)
	if filename.endswith(".txt") :
		with open(filename, 'r') as test :
			
			testfile = "";

			# Skip until line is an integer
			line = test.readline().strip()
			while isInt(line) == False:
				line = test.readline().encode('utf-8').strip()
				print(line)
				

			line = test.readline().strip()
			# Add lines until end of text body
			while line != '-------' :
				testfile += (line + " ")
				line = test.readline().strip()


			t, f = returnLists(testfile)
			print(t)
			print(f)
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

