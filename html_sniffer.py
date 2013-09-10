import urllib2,sys,re

heads = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}

request = urllib2.Request(sys.argv[1], headers=heads)
f = urllib2.urlopen(request)
# read html from url
html = f.read()
# remove html tags
html = re.sub('<[^<]+?>', '', html)
# remove multiple spaces (for better looking results)
html = " ".join(html.split())

# convert to lower case for case insensitive search
lower_string = html.lower()
result = lower_string.find(sys.argv[2].lower())
cmd_args = len(sys.argv)

if cmd_args > 3:
    # first offset argument
    offset_before = int(sys.argv[3])
else:
    offset_before = 0

if cmd_args > 4:
    # second offset argument
    offset_after = int(sys.argv[4])
else:
    offset_after = 100

if result != -1:
    print "String found!!!!"
    print "Part of the string with offsets defined"
    print "======================================="
    print html[result - offset_before:result + offset_after]
    print "======================================="
else:
    print "String not found (info: search is not case sensitive)"
