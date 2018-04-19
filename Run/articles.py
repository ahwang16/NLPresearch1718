# articles.py

import newspaper
import json, re, sys, time

# Find links in a given string
# Return links (number of links) and output (list of links)
def findLinks(given) :
	pat = re.escape('-._~:/?#\'[]@!$&()*+,;=%')
	found = re.findall('\(?(https?://\w*\.?[a-zA-Z0-9]*\.[A-Za-z0-9{}]*)\)?'.format(pat), given)
	output = []
	links = 0

	for s in found :
		if 'reddit' not in s :
			links += 1
			if (s[-1] == ')') :
				output.append(s[0:len(s) - 1] + "\n")
			elif (s[len(s)-2] == ')') :
				output.append(s[0:len(s) - 2] + "\n")
			else :
				output.append(s + "\n")


	return links, output

# Return list of Articles from given list of links
def findArticle(links) :
	articles = []

	for l in links :
		url = l.strip()		
		a = newspaper.Article(url, language='en')
		a.download()
		try :
			a.parse()
		except newspaper.article.ArticleException :
			print("Article not found")

	return articles, links 

# Write file given JSON object
def writeFile(data, title, isOP) :
	file.write(title + '\n')
	if isOP :
		file.write("OP\n")
	file.write("ID: " + data['id'] + '\n')
	file.write("Author: " + data['author'] + '\n\n')

def writeReport(linkList) :
	for l in linkList :
		report.write(l + '\n')

f = 0

report = open('report.txt', 'w')
linkPosts = 0 # number of posts containing a link
totalPosts = 0 # total number of posts
OPlink = 0
totalLinks = 0

with open('cmv_20161111.jsonlist', 'r') as j :

	for line in j :

		data = json.loads(line)
		if data['created_utc'] >= 1478779199 :
			continue

		file = open(str(f) + '.txt', 'w')
		title = data['title'].upper()

		writeFile(data, title, True)

		
		# Write links and total number of links at the beginning of post
		links, output = findLinks(data['selftext'])
		for o in output :
			file.write(o + "\n")
		file.write(str(links) + '\n\n')
		if (links > 0) :
			linkPosts += 1
			OPlink += 1
		totalPosts += 1
		totalLinks += links


		file.write(data['selftext'] + '\n\n')
		file.write('-------' + '\n\n')


		articles, linkList = findArticle(output)
		l = 0

		# Write articles and links at the bottom of post
		for a in articles :
			file.write(linkList[l])
			file.write(a.title.upper() + '\n' + a.text.encode('utf-8') + '\n\n')
			file.write('-------' + '\n\n')
			l += 1

		writeReport(linkList)

		file.close()



		f += 1

		for comment in data['comments'] :
			if 'count' in comment :
				continue
			
			file = open(str(f) + '.txt', 'w')

			writeFile(comment, title, False)

			# Links and total number at beginning of post
			links, output = findLinks(comment['body'])
			for o in output :
				file.write(o.encode('utf-8') + "\n")
			file.write(str(links) + '\n\n')
			if (links > 0) :
				linkPosts += 1
			totalPosts += 1
			totalLinks += links 

			file.write(comment['body'].encode('utf-8') + '\n\n')
			file.write('-------' + '\n\n')

			articles, linkList = findArticle(output)
			l = 0

			# Articles and links at bottom
			for a in articles :
				file.write(linkList[l])
				file.write(a.title.upper() + '\n' + a.text.encode('utf-8') + '\n\n')
				file.write('-------' + '\n\n')
				l += 1

			writeReport(linkList)
			file.close()

			f += 1


report.write('\n\nOP links: ' + str(OPlink))
report.write('\nPosts with links: ' + str(linkPosts) + '\nTotal posts: ' + str(totalPosts))
report.write('\nTotal links: ' + str(totalLinks))




# read = open("links.txt", "r")

# for line in read :
# 	url = line.strip()
# 	print (line)
# 	a = Article(url, language='en')
# 	a.download()
# 	a.parse()

# 	print (a.title + "\n")
# 	print (a.text[:150])


# read.close()
