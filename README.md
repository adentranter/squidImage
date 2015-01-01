
#What?
The purpose of this script is to create an html file which images from a squid access log are loaded into img tags and outputed to standard html.

#How?
To run this script its simple.

	python main.py -i /var/log/squid/access.log -o output.html 

To view all the options use the 

	python main.py -h

###Example output
![Screenshot of example output](http://2.bp.blogspot.com/-WJH3TISCMEg/UO_0o8NIlPI/AAAAAAAAAD0/eUUC-Cu_U_o/s640/Screenshot+from+2013-01-11+21:16:01.png  "Screenshot of example output")


#Advanced use?
this command shows how you can tell how many images to load and what IP to look for.

	python main.py -i /var/log/squid/access.log -o output.html -x <amount> -a <ip> 



Copyright (C) 2014  Aden Tranter


