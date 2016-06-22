
#!/usr/bin/python
# -*- coding: UTF-8 -*-

inputfile = open("readandwrite.txt", 'r+')
# outputfile = open("README.md", 'w')
count = 0
while(1):
   teststr = inputfile.readline().strip('\n')
   if not teststr:
      break
   
   teststr = teststr + " this is a add on\n"
   # inputfile.seek(0)
   # inputfile.write(teststr)
   print teststr
   count += 1
print count