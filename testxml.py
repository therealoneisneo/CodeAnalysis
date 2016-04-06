#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import sys


# DOMTree = xml.dom.minidom.parse("full_coverage.xml")
DOMTree = xml.dom.minidom.parse(sys.argv[1])
collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
# if collection.hasAttribute("shelf"):
#    print "Root element : %s" % collection.getAttribute("shelf")


# movies = collection.getElementsByTagName("movie")
lines = collection.getElementsByTagName("line")

for line in lines:
   print "*****line*****"
   # if line.hasAttribute("number"):
      # print "Line Number: %s" % movie.getAttribute("number")
   # print line
   lineNum = line.getAttribute("number")
   hits = line.getAttribute("hits")
   print "Line Number: %s" % lineNum
   print "hits: %s" % hits
   # break

   # type = movie.getElementsByTagName('type')[0]
   # print "Type: %s" % type.childNodes[0].data
   # format = movie.getElementsByTagName('format')[0]
   # print "Format: %s" % format.childNodes[0].data
   # rating = movie.getElementsByTagName('rating')[0]
   # print "Rating: %s" % rating.childNodes[0].data
   # description = movie.getElementsByTagName('description')[0]
   # print "Description: %s" % description.childNodes[0].data