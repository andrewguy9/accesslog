import docopt
import json
import fileinput
from sys import stdout, stderr

from accesslog import DictReader, TupleReader, whitespace_splitter, regex_splitter_factory

__doc__ = \
"""
Convert acccess logs into json dictionaries.

Usage:
  log2dict [--regex=<pattern>] <fields> [<files>...]

Options:
  <fields>  Comma delimited list of field names.
  <files>   List of files to read.
"""

def hook_nobuf(filename, mode):
  return open(filename, mode, 0)

def main():
  args = docopt.docopt(__doc__)
  if args['--regex']:
    splitter = regex_splitter_factory(args['--regex'])
  else:
    splitter = whitespace_splitter
  fields = args['<fields>'].split(",")
  logs = fileinput.input(args['<files>'], openhook=hook_nobuf)
  reader = iter(DictReader(fields, logs, splitter))

  while True:
    try:
      record = next(reader)
      stdout.write(json.dumps(record))
      stdout.write("\n")
      stdout.flush()
    except StopIteration:
      break
    except ValueError as e:
      stderr.write(str(e))

