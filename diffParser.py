"""module parsing the diff.txt file"""
__author__ = "jinlong Frank Feng"

import os
import string



def rindex(list, target):
	n = len(list)
	for i in reversed(range(n)):
		# print list[i]
		if list[i] == target:
			return i
	return -1

class LineInstances: # the class of a line instance in diff


	def __init__(self):
		self.insID = None # the id
		self.project_name = None # the project this file belongs to
		self.bug_ID = None # the bug ID within this project
		self.filename = None # the file being compared
		self.line_num = None
		self.isBuggy = False # boolean value indicate whether this line is buggy
		
		return

	def setValue(self, insID, project, bugID, FileName, line_num, isBuggy = False):
		self.insID = insID
		self.project_name = project
		self.bug_ID = bugID
		self.filename = FileName
		self.line_num = line_num
		self.isBuggy = isBuggy

		return

	# def copy(self, instances):
	# 	self.setValue(instances.FileName, instances.trainL, instances.testL, instances.Vec)
	# 	return

	def display(self): # show it self
		print self.insID
		print self.project_name
		print self.bug_ID
		print self.filename
		print self.line_num
		print self.isBuggy
		return

class parser: # the instance to parse the .cov file
	def __init__(self):
		# self.InstanceDic = {} # the dictionary for all parsed instances
		# self.instance_num = 0 # count of the number if instances parsed
		# self.InstancList = [] # the list of all parsed instances
		return


	def readFile(self, filename): # read a single .cov file

		inputfile = open(filename)
		# CovType = filename.split('.')[-2].split('-')[-1]
		# FileName = filename.split('/')[-1]
		# count = -1

		while(1):
			tempstring = inputfile.readline()
			if not tempstring:
				break
			if not len(tempstring):
				continue

			tempstring = tempstring.strip()
			tempstring = tempstring.split()
			t_size = len(tempstring)
			TestName = tempstring[0]

			for i in range(1, t_size):
				tempIns = CovInstances()
				parsestring = tempstring[i].strip()
				ID = self.instance_num
				OriString = tempstring[i]
				ind1 = tempstring[i].rindex('.')
				ClassName = tempstring[i][0:ind1]
				ind2 = tempstring[i].rindex(')')
				Method = tempstring[i][ind1 + 1:ind2 + 1]

				# print tempstring[i]
				
				LineNum = None
				if CovType == "meth":
					# ReturnType = None
					ReturnType = tempstring[i][rindex(tempstring[i], ')') + 1 : rindex(tempstring[i], '-')]
				else:
					ReturnType = tempstring[i][rindex(tempstring[i], ')') + 1 : rindex(tempstring[i], ':')]
					LineNum = tempstring[i][rindex(tempstring[i], ':') + 1 : rindex(tempstring[i], '-')]
				Count = tempstring[i][rindex(tempstring[i], '-') + 1 :]
				tempIns.setValue(ID, OriString, TestName, CovType, ClassName, ReturnType, Count, Method, FileName, LineNum)
				self.InstanceDic[OriString] = tempIns
				self.InstancList.append(tempIns)
				self.instance_num += 1
				# tempIns.display()

		inputfile.close()
		return
	def loadDir(self, dirName): # load the .cov file in the whole directory
		for root, dirs, files in os.walk(dirName):
			# for d in dirs: 
			# 	print os.path.join(root, d)
			for f in files:
				if f[rindex(f,'.') + 1:] == "cov":
					print "Processing file : " + os.path.join(root, f) + "..."
					self.readFile(os.path.join(root, f))
		print len(self.InstancList)
		return

	def write2File(self, filename):
		outfile = open(filename, 'w')
		print "Writing to file  " + filename + "..."
		outfile.write("ID,Filename,test_name,cov_type,classname,Method,return,cov-count,line_num,original_record\n")
		for item in self.InstancList:
			tempstring = str(item.insID) + "," + str(item.filename) + "," + str(item.test_name) + "," + str(item.cov_type) + "," + str(item.classname) + "," + str(item.method) + "," + str(item.return_type) + "," + str(item.cov_count) + "," + str(item.line_num) + "," + str(item.original_record) +"\n"
			outfile.write(tempstring)
		outfile.close()
		return

if __name__ == "__main__":
	Parser = parser()
	# Parser.readFile("Ant0.0-test-elem.cov")
	Parser.loadDir("/if22/br8jr/BitBuckets/uva_git/rtp/cov-data/")
	# Parser.loadDir("../rtptest/cov-data/")
	Parser.write2File("test.csv")


