# newdocs.py

import os.path, re

pathD = "/Volumes/USB/Research 2017-2018/RunNew"
pathS = "/Volumes/USB/Research 2017-2018/Run"

# for file in os.listdir(pathS) :
# 	if re.match(r"\d+\.txt", file) :
# 		with open(file, 'r') as test :
# 			filename = re.split("(\d+)", str(file))
# 			filename = str(filename[1])

# 			completeName = os.path.join(pathD, filename + "_post.txt")
# 			print(completeName)
# 			text = test.read()
# 			textedit = re.split(r"\n\n\d+\n\n", text)
# 			text = textedit[1]


# 			text = re.split("-------", text)


# 			with open(completeName, 'w') as current :
# 				current.write(text[0])


# 			count = 1
# 			completeName = os.path.join(pathD, filename + "_" + str(count) + "_article.txt")
# 			for x in range (1, len(text) - 1) :
# 				with open(completeName, 'w')  as current :
# 					current.write(text[x])
# 					count += 1
# 					print(completeName)


total = open(os.path.join(pathD, "total.txt"), 'w')
for file in os.listdir(pathD) :
	with open(os.path.join(pathD, file), 'r') as test :
		total.write(test.read())
total.close()
