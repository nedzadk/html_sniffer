#!/usr/bin/python
import urllib2
import sys
import re
import parser

heads = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) \
          AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64',
         'Accept': 'text/html,application/xhtml+xml, \
          application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}

request = urllib2.Request(sys.argv[1], headers=heads)
f = urllib2.urlopen(request)
# read html from url
html = f.read()
# remove multiple spaces (for better looking results)
html = " ".join(html.split())
# convert to lower case for case insensitive search
lower_string = html.lower()
result = 0
items = []
# Loop through html for multpiple search
while result < len(html):

    result = lower_string.find(sys.argv[2].lower(), result)
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
        # Uncomment for dirty result (debug)
        # print html[result - offset_before:result + offset_after]
        # Calling strip_string function that cleans result and do some other
        # cleaning
        final_text = re.sub('<[^<]+?>', '', parser.strip_string(html, result))
        # Strip whitespaces and compare the size, show only if result is bigger
        # than length of the searched word
        if len(final_text.strip()) > len(sys.argv[2]):
            # Check if found string already exist
            if final_text.strip() not in items:
                # Check again if result contains searched term
                if final_text.lower().find(sys.argv[2].lower()) != -1:
                    # If everything OK add it to list
                    items.append(final_text.strip())
    else:
        # Display found data
        if len(items) < 1:
            print "Nothing found"
        else:
            x = 1
            parser.write_to_db(items)
            for item in items:
                print x, item
                x += 1
        break

    result += len(sys.argv[2])
