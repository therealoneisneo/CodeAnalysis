"""filter the {proj}TestMethodsAll.txt and list up all methods"""
__author__ = "jinlong Frank Feng"


import sys
import os

# if len(sys.argv) < 3:
# 		print "Usage: python <raw_list.txt> <filtered_list.txt>"
# 		sys.exit()
# 	inputfile = sys.argv[1]
# 	outputfile = sys.argv[2]

infilename = "ChartTestMethodsAll_raw.txt"
outfilename = "test.txt"

inputfile = open(infilename)
outfile = open(outfilename, 'w')

while(1):

	tempstring = inputfile.readline()
	if not tempstring:
		break

	tempstring = tempstring.strip()

	if not len(tempstring):
		continue
	if tempstring.split()[0] == "bugindex":
		# print tempstring
		bugindex = tempstring.split()[2]
		# print bugindex
	if tempstring.split()[0] == "public" and tempstring.split()[1] == "class":
		testClass = tempstring.split()[2]
	if tempstring.split()[0] == "public" and tempstring.split()[1] == "void":
		if tempstring.split()[2][:4] == "test":
			methodName = tempstring.split()[2][:-3]
			# print bugindex
			# print testClass
			# print methodName
			outstr = bugindex + ' ' + testClass + "::" + methodName

			outfile.write(outstr + '\n')
			# break

		


# root = "/localtmp/feng/Checkedout"
# project = "Chart"
# proj_dir = root + '/' + project + '/'
# # os.listdir(currentdir)
# for bugindex in range(1,27):
# 	currentdir = proj_dir + str(bugindex) + '/buggy/build-tests/org/jfree/chart/'

# # dirname = sys.argv[1]


# 	result = [os.path.join(dp, f) for dp, dn, fs in os.walk(currentdir) for f in fs if os.path.splitext(f)[1] == '.class']
# 	for fname in result:
# 		print str(bugindex) + ' ' + fname
