'''statistical analysis of coverage csv file to get the result of e_f, e_p, n_f and n_p, need pass in 3 arguments: indicate the input file and output file as well as the largest bugId as the upper bound, this script process one buggy version at a time.'''
__author__ = "jinlong Frank Feng"



import sys
import os
import math



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


# 25 different metrics:
def Tarantula(e_f,e_p,n_f,n_p):
	if e_f == 0:
		return 0
	else:
		term1 = float(e_f)/(e_f + n_f)
	if e_p == 0:
		term2 = 0
	else:
		term2 = float(e_p)/(e_p + n_p)
	return term1/(term1 + term2)

def Ochiai(e_f,e_p,n_f,n_p):
	if e_f == 0:
		return 0
	term = math.sqrt((e_f + e_p) * (e_f + n_f))
	return float(e_f) / term

def Ochiai_2(e_f,e_p,n_f,n_p):
	term = (e_f + e_p) * (n_f + n_p) * (e_f + n_p) * (e_p + n_f)
	if term == 0:
		return 0
	return float(e_f * n_p) / math.sqrt(term)

def Jaccard(e_f,e_p,n_f,n_p):
	return float(e_f) / (e_f + e_p + n_f)

def Ample(e_f,e_p,n_f,n_p):
	if e_f + n_f == 0:
		print e_f
		print n_f
	term1 = float(e_f) / (e_f + n_f)
	term2 = float(e_p) / (e_p + n_p)
	return abs(term1 - term2)

def RussellRao(e_f,e_p,n_f,n_p):
	return float(e_f) / (e_f + e_p + n_f + n_p)

def Hamann(e_f,e_p,n_f,n_p):
	term1 = e_f + n_p - e_p - n_f
	term2 = e_f + e_p + n_f + n_p
	return float(term1) / term2

def SorensenDice(e_f,e_p,n_f,n_p):
	return float(2 * e_f) / (2 * e_f + e_p + n_f)

def Dice(e_f,e_p,n_f,n_p):
	return float(2 * e_f) / (e_f + e_p + n_f)

def Kulczynski_1(e_f,e_p,n_f,n_p):
	return float(e_f) / (n_f + e_p)

def Kulczynski_2(e_f,e_p,n_f,n_p):
	term1 = float(e_f) / (e_f + n_f)
	term2 = float(e_f) / (e_f + e_p)
	return (term1 + term2) / 2

def SimpleMatching(e_f,e_p,n_f,n_p):
	return float(e_f + n_p) / (e_f + e_p + n_f + n_p)

def Sokal(e_f,e_p,n_f,n_p):
	return float(e_f + n_p) * 2 / (e_f * 2 + e_p + n_f + n_p * 2)

def M1(e_f,e_p,n_f,n_p):
	return float(e_f + n_p) / (n_f + e_p)

def M2(e_f,e_p,n_f,n_p):
	return float(e_f) / (e_f + e_p * 2 + n_f * 2 + n_p)

def RogersTanimoto(e_f,e_p,n_f,n_p):
	return float(e_f + n_p) / (e_f + e_p * 2 + n_f * 2 + n_p)

def Goodman(e_f,e_p,n_f,n_p):
	return float(2 * e_f - n_f - n_p) / (2 * e_f + n_f + n_p)

def Hamming(e_f,e_p,n_f,n_p):
	return (e_f + n_p)

def Euclid(e_f,e_p,n_f,n_p):
	return math.sqrt(e_f + n_p)

def Overlap(e_f,e_p,n_f,n_p):
	minv = min(e_f, e_p, n_f)
	if minv == 0:
		return 0
	else:
		return float(e_f) / minv

def Anderberg(e_f,e_p,n_f,n_p):
	return float(e_f) / (e_f + 2 * e_p + 2 * n_f)

def Zoltar(e_f,e_p,n_f,n_p):
	if e_f == 0:
		return 0
	else:
		return float(e_f) / (e_f + e_p + n_f + float(10000 * n_f * e_p) / e_f)

def Wong_1(e_f,e_p,n_f,n_p):
	return e_f

def Wong_2(e_f,e_p,n_f,n_p):
	return e_f - e_p

def Wong_3(e_f,e_p,n_f,n_p):
	if e_p <= 2:
		h = e_p
	elif e_p <= 10:
		h = 2 + 0.1 * (e_p - 2)
	else:
		h = 2.8 + 0.01 * (e_p - 10)
	return e_f - h



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

outputfile.write("idx,BugId,FileName,LineNo,e_f,e_p,n_f,n_p,Tarantula,Ochiai,Ochiai_2,Jaccard,Ample,RussellRao,Hamann,SorensenDice,Dice,Kulczynski_1,Kulczynski_2,SimpleMatching,Sokal,M1,M2,RogersTanimoto,Goodman,Hamming,Euclid,Overlap,Anderberg,Zoltar,Wong_1,Wong_2,Wong_3\n")

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
		#idx,BugId,FileName,LineNo,e_f,e_p,n_f,n_p,Tarantula,Ochiai,Ochiai_2,Jaccard,Ample,RussellRao,Hamann,SorensenDice,Dice,Kulczynski_1,Kulczynski_2,SimpleMatching,Sokal,M1,M2,RogersTanimoto,Goodman,Hamming,Euclid,Overlap,Anderberg,Zoltar,Wong_1,Wong_2,Wong_3
		e_f = current.failed
		e_p = current.total - current.failed
		n_f = ftestnum - current.failed
		n_p = testnum - ftestnum - current.total + current.failed

		outputfile.write(str(count) + ',' + str(currentBugId) + ',' + current.filename_lineNo.split('_')[0] + ',' + current.filename_lineNo.split('_')[1] + ',' + str(e_f) + ',' + str(e_p) + ',' + str(n_f) + ',' + str(n_p) + ',' + str(Tarantula(e_f,e_p,n_f,n_p)) + ',' + str(Ochiai(e_f,e_p,n_f,n_p)) + ',' + str(Ochiai_2(e_f,e_p,n_f,n_p)) + ',' + str(Jaccard(e_f,e_p,n_f,n_p)) + ',' + str(Ample(e_f,e_p,n_f,n_p)) + ',' + str(RussellRao(e_f,e_p,n_f,n_p)) + ',' + str(Hamann(e_f,e_p,n_f,n_p)) + ',' + str(SorensenDice(e_f,e_p,n_f,n_p)) + ',' + str(Dice(e_f,e_p,n_f,n_p)) + ',' + str(Kulczynski_1(e_f,e_p,n_f,n_p)) + ',' + str(Kulczynski_2(e_f,e_p,n_f,n_p)) + ',' + str(SimpleMatching(e_f,e_p,n_f,n_p)) + ',' + str(Sokal(e_f,e_p,n_f,n_p)) + ',' + str(M1(e_f,e_p,n_f,n_p)) + ',' + str(M2(e_f,e_p,n_f,n_p)) + ',' + str(RogersTanimoto(e_f,e_p,n_f,n_p)) + ',' + str(Goodman(e_f,e_p,n_f,n_p)) + ',' + str(Hamming(e_f,e_p,n_f,n_p)) + ',' + str(Euclid(e_f,e_p,n_f,n_p)) + ',' + str(Overlap(e_f,e_p,n_f,n_p)) + ',' + str(Anderberg(e_f,e_p,n_f,n_p)) + ',' + str(Zoltar(e_f,e_p,n_f,n_p)) + ',' + str(Wong_1(e_f,e_p,n_f,n_p)) + ',' + str(Wong_2(e_f,e_p,n_f,n_p)) + ',' + str(Wong_3(e_f,e_p,n_f,n_p)) + "\n")
		count += 1


	inputfile.seek(0) # return to the begining of file



inputfile.close()
outputfile.close()



