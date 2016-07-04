#!/usr/bin/python

"""module parsing the diff.txt file"""
__author__ = "jinlong Frank Feng"

import sys
import os
import string

class parser: # the instance to parse the .cov file
	def __init__(self):

		return

	def parseFile(inputfile, outputfile):
		inputfile = open(infilename)
		outfile = open(outfilename, 'w')
		return

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Usage: python <diff_file.txt> <output_file.csv>"
		sys.exit()
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]

	Parser = parser()
	# Parser.readFile("Ant0.0-test-elem.cov")
	Parser.parseFile(inputfile, outputfile)
	# Parser.loadDir("../rtptest/cov-data/")
	# Parser.write2File("test.csv")