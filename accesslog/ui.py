import docopt
import json
import fileinput
import sys
import argparse
from accesslog import DictReader, TupleReader, whitespace_splitter, regex_splitter_factory

__doc__ = \
"""
Convert acccess logs into json dictionaries.

Usage:
  log2dict --regex=<pattern> <fields> [<files>...]

Options:
  <fields>  Comma delimited list of field names.
  <files>   List of files to read.
"""

def main():
  args = docopt.docopt(__doc__)
  if args['--regex']:
    splitter = regex_splitter_factory(args['--regex'])
  else:
    splitter = whitespace_splitter
  fields = args['<fields>'].split(",")
  logs = fileinput.input(args['<files>'])
  reader = DictReader(fields, logs, splitter)
  for record in reader:
    print json.dumps(record)

