import sys
from pymongo import MongoClient

def write_to_db(items):
    db = MongoClient()
    watchit_db = db.watchit4_me
    table = watchit_db.search_results
    for item in items:
        entry = ({"site": sys.argv[1], "result": item})
        table.insert(entry)


def strip_string(text, starting_offset):
    x = starting_offset
    found = False
    new_text = ""
    while (found is not True):
        x -= 1
        if text[x] != '>':
            new_text = new_text + text[x]
        else:
            found = True

    x = starting_offset
    found = False
    new_text2 = ""
    while (found is not True):
        x += 1
        if text[x] != '<':
            new_text2 = new_text2 + text[x]
        else:
            found = True
    # Revers first part of the result when returning result
    return new_text[::-1] + text[starting_offset] + new_text2


