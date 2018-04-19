# adjustFileNames.py

import os

x = 0

directory = "/Volumes/USB/Research 2017-2018/Run"

print(os.listdir(directory))

# for file in os.listdir(directory) :
# 	if '.txt' in file.decode('utf-8') :
# 		os.rename(file, str(x) + '.txt')
# 		x += 1