import urllib2,sys,re

f = urllib2.urlopen(sys.argv[1]) #Load URL from first command line argument
html = f.read() # Read html from url
html = re.sub('<[^<]+?>','',html) # Remove HTML tags
html = " ".join(html.split()) #Remove multiple spaces

lower_string = html.lower() # Convert to lower case for case insesitiv search
pocetak = lower_string.find(sys.argv[2].lower()) #Find string index (if string exist)
cmd_args = len(sys.argv)

if cmd_args>3:
    offset_before = int(sys.argv[3]) #String offset argument (for displaying string
else:
    offset_before = 0

if cmd_args>4:
    offset_after = int(sys.argv[4])  #Same as above
else:
    offset_after = 100

if pocetak>-1:
    print "String found"
    print "Part of the string with offsets defined"
    print html[pocetak-offset_before:pocetak+offset_after]
else:
    print "String not found (info: search is not case sensitive)"   
