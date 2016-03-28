'''after out put the bug info to a .txt, use this python script to extract the source code filename related with these bugs. Usage: need pass in 2 arguments: indicate the input file and output file'''
'''update: add test method name, controled by the third argument 1: source name 2: test method name 3: all '''

__author__ = "jinlong Frank Feng"


import sys


if len(sys.argv) < 3:
	print "error : need 2 arguments!"
	exit()

in_filename = sys.argv[1]
out_filename = sys.argv[2]
out_type = int(sys.argv[3])

inputfile = open(in_filename)
outputfile = open(out_filename, 'w')

num_of_bugs = -1
bug_index = 0
SourceMarker = False # indicator of the parsing start of source file name
TestMarker = False # indicator of the starting of the parsing of test method class and name


while(1):
	tempstring = inputfile.readline()
	if not tempstring:
		break
	if not len(tempstring):
		continue

	tempstring = tempstring.strip()

	if num_of_bugs < 0:
		if tempstring[:16] == "Number of bugs: ":
			num_of_bugs = int(tempstring[16:])
			print "extracting the "+ str(num_of_bugs) +" names of source code from " + in_filename + "..."

# parsing the test method name
	
	if (out_type == 2 or out_type == 3):

		if tempstring == "Root cause in triggering tests:":
			TestMarker = True
			bug_index += 1
			continue
		if tempstring[:15] == "-----------------------"[:15]:
			TestMarker = False
			continue
		if TestMarker and tempstring[:2] == "- ":
			test_name = str(bug_index) + " " + tempstring.split(' ')[-1]
			outputfile.write(test_name)
			outputfile.write('\n')
			print test_name


# parsing the source filename
	if (out_type == 1 or out_type == 3):

		if tempstring == "List of modified sources:":
			SourceMarker = True
			# bug_index += 1
			continue
		if tempstring[:15] == "-----------------------"[:15]:
			SourceMarker = False
			continue
		if SourceMarker:
			source_name = str(bug_index) + " " + tempstring.split(' ')[-1] + ".java"
			outputfile.write(source_name)
			outputfile.write('\n')
			print source_name
			

inputfile.close()
outputfile.close()





