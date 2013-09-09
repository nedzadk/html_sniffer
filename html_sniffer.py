import urllib2,sys,re

heads = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}

request = urllib2.Request(sys.argv[1],headers=heads) #Request to site with headers
f = urllib2.urlopen(request)
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
    print "======================================="
    print html[result-offset_before:result+offset_after] #Show string based on defined offsets
    print "======================================="
else:
    print "String not found (info: search is not case sensitive)"   
