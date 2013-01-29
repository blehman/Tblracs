Tblracs
=======

Gnip normalized Tumblr activities parser.

Install with,
pip install tblracs

tblracs.py takes 0 or more arguments and reads 1 or more JSON Tumblr
activities from standard input.  The activities are parsed and 
output is pipe-delimited records representing a subset of the activity
fields.

Usage: tblracs.py [options]

Options:
  -h, --help       show this help message and exit
  -u, --user       Include user fields
  -s, --structure  Include reblog linking fields
  -r, --rules      Include rules fields
  -l, --lang       Include language fields
  -p, --pretty     Pretty JSON output of full records
  -c, --csv        Comma-delimited output (default is | without quotes)
