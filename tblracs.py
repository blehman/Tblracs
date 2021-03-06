#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__="Scott Hendrickson"
__license__="Simplified BSD"
import sys
import codecs
import fileinput
from optparse import OptionParser
import tblracscsv.tblracscsv

# unicode
reload(sys)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

parser = OptionParser()
parser.add_option("-u", "--user", action="store_true", dest="user", default=False, help="Include user fields")
parser.add_option("-s", "--structure", action="store_true", dest="struct", default=False, help="Include reblog linking fields")
parser.add_option("-r", "--rules", action="store_true", dest="rules", default=False, help="Include rules fields")
parser.add_option("-l", "--lang", action="store_true", dest="lang", default=False, help="Include language fields")
parser.add_option("-p", "--pretty", action="store_true", dest="pretty", default=False, help="Pretty JSON output of full records")
parser.add_option("-c", "--csv", action="store_true", dest="csv", default=False, help="Comma-delimited output (default is | without quotes)")
(options, args) = parser.parse_args()

if options.csv:
    delim = ","
else:
    delim = "|"
dcsv = tblracscsv.tblracscsv.TblrCSV(delim, options.user, options.rules, options.lang, options.struct, options.pretty)
for record in fileinput.FileInput(args,openhook=fileinput.hook_compressed):
    if record == "":
        continue
    sys.stdout.write("%s\n"%dcsv.procRecord(record))
