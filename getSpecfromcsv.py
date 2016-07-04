'''statistical analysis of coverage csv file to get the result of e_f, e_p, n_f and n_p, need pass in 3 arguments: indicate the input file and output file as well as the bugId, this script process one buggy version at a time.'''
__author__ = "jinlong Frank Feng"



import sys
import os

class Entity():
	def __init__(self, filename_lineNo):
		# self.bugId = bugId
		self.filename_lineNo = filename_lineNo
		# self.lineNo = lineNo
		self.total = 1 #count for total testcases
		self.failed = 0 #count for failed testcases
		# e_f = None
		# e_p = None
		# n_f = None
		# n_p = None
		# self.rawdata = raw # the original parsed data




if len(sys.argv) < 3:
	print "error : need 3 arguments!"
	print "Usage : python getSpecfromcsv.py <inputfile.csv> <outputfile.csv> Largets_bugID"
	exit()

in_filename = sys.argv[1]
out_filename = sys.argv[2]
bugrange = int(sys.argv[3])

# in_filename = "cov_csv_all.csv"
# out_filename = "spectrum.csv"

# bugrange = 26

if in_filename[-3:] != "csv":
	print "wrong input file..."
	exit()

inputfile = open(in_filename)
outputfile = open(out_filename, 'w')

outputfile.write("idx,BugId,FileName,LineNo,e_f,e_p,n_f,n_p\n")

count = 0

for currentBugId in range(1, bugrange + 1):
	print "processing " + str(currentBugId) + " of " + str(bugrange) + " version..."
	entityset = {}# the dic for all instances, key is filename + lineNo
	total_test = set() # set of all test cases within this buggy version
	total_fail = set() # set of failed test cases
	while(1):
		tempstring = inputfile.readline()
		if not tempstring:
			break
		if not len(tempstring):
			continue
		parse = tempstring.strip().split(',')#tags in the csv file: idx,ProjectName,BugId,FileName,MethodName,TestName,LineNo,Hits,isPass

		if parse[2] != str(currentBugId):
			continue
		
		tempKey = parse[3] + '_' + parse[6]
		if entityset.has_key(tempKey):
			entityset[tempKey].total += 1
			if parse[-1] != "True":
				entityset[tempKey].failed += 1
				# print parse
				# print "False!"
		else:
			entityset[tempKey] = Entity(tempKey)

		total_test.add(parse[5])
		if parse[-1] == "False":
			total_fail.add(parse[5])
		# if len(total_test) > 1:
		# 	break
		
	testnum = len(total_test)
	ftestnum = len(total_fail)
	for item in entityset:
		current = entityset[item]
		#idx,BugId,FileName,LineNo,e_f,e_p,n_f,n_p
		outputfile.write(str(count) + ',' + str(currentBugId) + ',' + current.filename_lineNo.split('_')[0] + ',' + current.filename_lineNo.split('_')[1] + ',' + str(current.failed) + ',' + str(current.total - current.failed) + ',' + str(ftestnum - current.failed) + ',' + str(testnum - ftestnum - current.total + current.failed) + "\n")
		count += 1


	inputfile.seek(0) # return to the begining of file



inputfile.close()
outputfile.close()



