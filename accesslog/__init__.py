import re

__doc__ = \
"""
accesslog.py - read access logs.
"""

def whitespace_splitter(line):
  return whitespace_splitter.whitespace_pattern.split(line)
whitespace_splitter.whitespace_pattern = re.compile("\s+")

def regex_splitter_factory(pattern):
  p = re.compile(pattern)
  def regex_splitter(line):
    match = p.match(line)
    if match is None:
      raise ValueError("Failed to match: %s" % line)
    return match.groups()
  return regex_splitter

class TupleReader:
  def __init__(self, f, fieldsplitter=whitespace_splitter):
    self.f = f
    self.splitter = fieldsplitter

  def __iter__(self):
    return self

  def next(self):
    line = self.f.readline()
    if line == "":
      raise StopIteration
    return self.splitter(line)

class DictReader:
  def __init__(self, fields, *args, **kwargs):
    self.tuple_reader = TupleReader(*args, **kwargs)
    self.fields = fields

  def __iter__(self):
    return self

  def next(self):
    datas = self.tuple_reader.next()
    return dict(zip(self.fields, datas))

