'''after out put the bug info to a .txt, use this python script to extract the source code filename related with these bugs'''
__author__ = "jinlong Frank Feng"


import sys


if len(sys.argv) < 3:
	print "error : need 2 arguments!"
	exit()

in_filename = sys.argv[1]
out_filename = sys.argv[2]

inputfile = open(in_filename)
outputfile = open(out_filename, 'w')

num_of_bugs = -1
bug_index = 0
filemarker = False


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
	if tempstring == "List of modified sources:":
		filemarker = True
		bug_index += 1
		continue
	if tempstring[:15] == "-----------------------"[:15]:
		filemarker = False
		continue
	if filemarker:
		source_name = str(bug_index) + " " + tempstring.split(' ')[-1] + ".java"
		outputfile.write(source_name)
		outputfile.write('\n')
		print source_name
		

inputfile.close()
outputfile.close()





