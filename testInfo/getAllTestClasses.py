"""List up all the test classes within project Chart"""
__author__ = "jinlong Frank Feng"


import sys
import os


root = "/localtmp/feng/Checkedout"
project = "Chart"
proj_dir = root + '/' + project + '/'
# os.listdir(currentdir)
for bugindex in range(1,27):
	currentdir = proj_dir + str(bugindex) + '/buggy/build-tests/org/jfree/chart/'

# dirname = sys.argv[1]


	result = [os.path.join(dp, f) for dp, dn, fs in os.walk(currentdir) for f in fs if os.path.splitext(f)[1] == '.class']
	for fname in result:
		print str(bugindex) + ' ' + fname
