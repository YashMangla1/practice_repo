import os
import sys

files_count=int(sys.argv[1])

for i in range(files_count):
	os.system("touch {}.py".format(i+1))
	os.system("echo \"print('{} file')\" >{}.py ".format(i+1,i+1))

 


