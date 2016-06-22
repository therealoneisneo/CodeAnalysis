# outfile.write("idx,ProjectName,BugId,FileName,MethodName,TestName, LineNo,Hits,isPass\n")

"""compile all parsed coverage csv file into one file"""
__author__ = "jinlong Frank Feng"

import sys
import os


rootdir = "Checkedout"

# rootdir = "../Verify_coverage"
count = 0
for proj in ["Chart"]: #,"Time","Lang","Closure","Math"]:
	currentdir = os.path.join(rootdir, proj)
	buggyfile = open("buginfo/" + proj + "TestName.txt", 'r')
	lookup = []
	while(1):
		tempstring = buggyfile.readline()
		if not tempstring:
			break
		temp = []
		temp.append(tempstring.split()[0])
		tempstring = tempstring.split()[1].split('::')
		temp.append(tempstring[0])
		temp.append(tempstring[1])
		lookup.append(temp)
	



	# currentdir = os.path.join(currentdir, "covInfo")

	targetfile = currentdir + "/cov_csv_all.csv"
	currentdir = os.path.join(currentdir, "cov_csv")
	outfile = open(targetfile, 'w')
	outfile.write("idx,ProjectName,BugId,FileName,MethodName,TestName, LineNo,Hits,isPass\n")
	for item in os.listdir(currentdir):

		if item[-3:] == "csv":
			filepath = os.path.join(currentdir, item)
			inputfile = open(filepath)
			print filepath
			while(1):
				tempstring = inputfile.readline()
				if not tempstring:
					break
				# tempstring = tempstring.strip()
				# if not len(tempstring):
				# 	continue
				sp = tempstring.split(',')
				if sp[0] != "idx":
					bugid = sp[2]
					testclass = sp[6].split('_')[0]
					testmethod = sp[6].split('_')[1]
					for item in lookup:
						if bugid == item[0] and testclass == item[1] and testmethod == item[2]:
							tempstring = tempstring.replace("True","False")
							break
					outfile.write(tempstring)
