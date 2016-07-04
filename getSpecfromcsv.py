'''statistical analysis of coverage csv file to get the result of e_f, e_p, n_f and n_p, need pass in 3 arguments: indicate the input file and output file as well as the bugId, this script process one buggy version at a time.'''
__author__ = "jinlong Frank Feng"



import sys
import os

class Entity():
	def __init__(self, filename, lineNo):
		# self.bugId = bugId
		self.filename_lineNo = filename + '_'+ lineNo
		# self.lineNo = lineNo
		passed = 0 #count for passed testcase and failed testcase
		failed = 0
		e_f = None
		e_p = None
		n_f = None
		n_p = None
		count = 0




# if len(sys.argv) < 3:
# 	print "error : need 2 arguments!"
# 	exit()

# in_filename = sys.argv[1]
# out_filename = sys.argv[2]
# currentBugId = sys.argv[3]

in_filename = "cov_csv_all.csv"
out_filename = "spectrum.csv"
currentBugId = "8"

if in_filename[-3:] != "csv":
	print "wrong input file..."
	exit()

inputfile = open(in_filename)
outputfile = open(out_filename, 'w')

tempstring = inputfile.readline() # read the first line of csv


inscountdic = {}

# passedtest = set()
# failedtest = set()

entityset = set()# the set for all entity

tempcount = 0

for currentBugId in range(1, bugrange + 1):

	while(1):
		tempstring = inputfile.readline()
		if not tempstring:
			break
		if not len(tempstring):
			continue
		parse = tempstring.split(',')#tags in the csv file: idx,ProjectName,BugId,FileName,MethodName,TestName,LineNo,Hits,isPass

		if parse[2] != currentBugId:
			continue

		# if parse[-1] == "True":
		# 	passedtest.add(parse[5])
		# else:
		# 	failedtest.add(parse[5])

		# tempIns = Entity(parse[3], parse[6])
		# tempkey = parse[3] + '_' + parse[6] + '_' + parse[5]
		# if inscountdic.has_key(tempkey):
		# 	inscountdic[tempkey] += 1
		# else:
		# 	inscountdic[tempkey] = 1
		# if tempcount > 1000:
		# 	break
		# tempcount += 1

	inputfile.seek(0)


inputfile.close()

# maxv = -1
# for item in inscountdic:
# 	if inscountdic[item] > maxv:
# 		maxv = inscountdic[item]
# print maxv

# test if a single file and line have multiple instance

	# if tempcount > 1000:
	# 	break
	# tempcount += 1


