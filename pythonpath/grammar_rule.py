import re

class GrammarRule:
  def __init__(self, pattern, suggestion, short_comment, full_comment, exceptions, ignore_case=True):
    if ignore_case:    
      self.pattern = re.compile(pattern, re.IGNORECASE)
    else:
      self.pattern = re.compile(pattern)
    
    self.suggestion = suggestion
    self.short_comment = short_comment                
    self.full_comment = full_comment
    self.exceptions = exceptions

  # short comment is displayed when user right clicks on squiggle
  # full comment appears when user runs grammar check


