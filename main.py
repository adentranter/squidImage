#!/usr/bin/python
import sys,re
from optparse import OptionParser

def main(argv):
	parser = OptionParser()
	parser.add_option("-i", "--input", dest="input",
        	          help="LOGFILE INPUTTING", metavar="INPUT")
	parser.add_option("-v", "--verbose",
        	          action="store_true", dest="verbose",
                	  help="print list of found images")
	parser.add_option("-o","--output",dest="output",
			help="HTML OUTPUT",metavar="OUTPUT")
	parser.add_option("-a","--address",dest="address",
			help="Target IP Address",metavar="target")
	parser.add_option("-x","--count",dest="count",
			help="Image Count")
	(options, args) = parser.parse_args()

	#test for input and out and if both are there, 
	if options.input is None or options.output is None:
		parser.print_help()
	else:
		squidImage(options.input,options.output,options.address,options.count,options.verbose)

def squidImage(inputFile,outFile,ip,countMax,verbose):
	log = inputFile
	output = outFile
	count = 0
		
	if countMax is None:
		countMax=200

	if verbose is None:
		verbose = False
	try:	
		fileout = open(output,"wb")
	except IOError:
   		print "Access denied to create output file"
	try:
		for line in reversed(open(log).readlines()):
			#check for ip
			if ip is not None:
				if not ip in line:
					line = ""

			#now extract the url
			src = re.search("(http|www)\S+(png|gif|jpe?g)", line)
			
			if src:
				src = src.group(0)
		
			if src: 
				fileout.write("<img src='")
				fileout.write(src)
				fileout.write("'/>")
				count+=1
				if verbose:
					print "Writing " 
					print src
		
			if int(countMax)<= int(count):
				break
	except IOError:
  		 print "Access denied to reading input file"	

	if count > 0:
		print "squidImage has finished, Found",str(count),"images."
	else:
		print "squidImage didn't find any images for your search"
	fileout.close()

if __name__ == "__main__":
   main(sys.argv[1:])


