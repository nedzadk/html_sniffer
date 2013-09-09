import urllib2,sys,re

f = urllib2.urlopen(sys.argv[1]) #Load URL from first command line argument
html = f.read() #Read html from url
html = re.sub('<[^<]+?>','',html) #Remove HTML tags
html = " ".join(html.split()) #Remove multiple spaces (better rading)

lower_string = html.lower() # Convert to lower case for case insensitiv search
result = lower_string.find(sys.argv[2].lower()) #Find string index (if string exist)
cmd_args = len(sys.argv)

if cmd_args>3:
    offset_before = int(sys.argv[3]) #First offset argument
else:
    offset_before = 0

if cmd_args>4:
    offset_after = int(sys.argv[4])  #Second offset argument
else:
    offset_after = 100

if result<>-1:
    print "String found!!!!"
    print "Part of the string with offsets defined"
    print html[result-offset_before:result+offset_after] #Show string based on defined offsets
else:
    print "String not found (info: search is not case sensitive)"   
