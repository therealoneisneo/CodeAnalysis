#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from xml.dom.minidom import parse
import xml.dom.minidom as dom
import sys
import os



def ParseXML(filename, proj):
	doc = dom.parse(filename)

	bugID = "testID"
	# outfilename = filename.split('/')[-1].split('.')[0] + ".csv"
	outfilename = filename[:-3] + "csv"
	outfile = open(outfilename, 'w')
	outfile.write("idx,ProjectName,BugId,LineNo,Hits,Branch\n")
	covClass = doc.getElementsByTagName("class")[0]
	# covClass = covClass.getElementsByTagName()
	methods = covClass.getElementsByTagName("methods")[0]
	methods = methods.getElementsByTagName("method")
	# print len(methods)
	# lineIns = []
	count = 0
	for method in methods:
		lineset = method.getElementsByTagName("line")
		for line in lineset:
			hits = line.getAttribute("hits")
			if hits != "0":
				outfile.write(str(count) + ',' + proj + ',' + bugID + ',' + line.getAttribute("number") + ',' + line.getAttribute("hits") + ',')
				# temp = LineCov(count, proj, bugID, line.getAttribute("number"), line.getAttribute("hits"))
				branch = line.getAttribute("branch")
				outfile.write(branch)
			# if branch == "true":
			#    condittions = 
			#    outfile.write(',' + )
			#condition process to be add
				outfile.write('\n')
				count += 1
	return






rootdir = "Checkedout"
count = 0
for proj in ["Chart","Time","Lang","Closure","Math"]:
	currentdir = os.path.join(rootdir, proj)
	currentdir = os.path.join(currentdir, "covInfo")
	for item in os.listdir(currentdir):
		if item[-3:] == "xml"
			filepath = os.path.join(currentdir, item)
			ParseXML(filepath, proj)
			print filepath
			count += 1
print count


