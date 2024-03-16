
from vsg import rule


class rule_localized_001(rule.rule):

  def __init__(self):
      super().__init__()
      self.name = 'localized' # Force the rule's name, because it can't be extracted from the module
      self.phase = 1
      self.fixable = False  # User must split the file
      self.solution = 'Split entity and architecture into separate files.'

  def analyze(self, oFile):
      if oFile.hasEntity and oFile.hasArchitecture:
          self.add_violation(1)
