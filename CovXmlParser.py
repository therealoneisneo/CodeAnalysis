#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from xml.dom.minidom import parse
import xml.dom.minidom as dom
import sys
import os



def ParseXML(filename, proj):
	doc = dom.parse(filename)

	bugID = filename.split("/")[-1].split("_")[0]
	# outfilename = filename.split('/')[-1].split('.')[0] + ".csv"
	start = filename.split("/")[-1].find("_")
	testname = filename.split("/")[-1][start + 1 : -4]
	# print testname
	outfilename = filename[:-3] + "csv"
	outfile = open(outfilename, 'w')
	outfile.write("idx,ProjectName,BugId,FileName,MethodName,TestName, LineNo,Hits,isPass\n")
	covClasses = doc.getElementsByTagName("class")
	count = 0
	for covClass in covClasses:
		FileName = covClass.getAttribute("filename")
		# covClass = covClass.getElementsByTagName()
		methods = covClass.getElementsByTagName("methods")[0]
		methods = methods.getElementsByTagName("method")

		for method in methods:
			methodName = method.getAttribute("name")
			lineset = method.getElementsByTagName("line")
			for line in lineset:
				hits = line.getAttribute("hits")
				if hits != "0":
					outfile.write(str(count) + ',' + proj + ',' + bugID + ',' +FileName + ',' + methodName + ',' + testname + ',' + line.getAttribute("number") + ',' + line.getAttribute("hits") + ',' + "False\n")
					# branch = line.getAttribute("branch")
					# outfile.write(branch)
					# outfile.write('\n')
					count += 1
	return






rootdir = "Checkedout"
# rootdir = "../Verify_coverage"
count = 0
for proj in ["Chart","Time","Lang","Closure","Math"]:
	currentdir = os.path.join(rootdir, proj)
	currentdir = os.path.join(currentdir, "covInfo")
	for item in os.listdir(currentdir):
		if item[-3:] == "xml":
			filepath = os.path.join(currentdir, item)
			ParseXML(filepath, proj)
			print filepath
			count += 1
print count

# currentdir = os.path.join(rootdir, "covInfo")
# for item in os.listdir(currentdir):
# 	if item[-3:] == "xml":
# 		filepath = os.path.join(currentdir, item)
# 		ParseXML(filepath, "Chart")
# 		print filepath
# 		count += 1
# 		# print count
# 		if count > 3:
# 			break



