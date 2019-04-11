
from vsg import rule


class rule_localized_001(rule.rule):

  def __init__(self):
      rule.rule.__init__(self, 'localized', '001')
      self.phase = 1
      self.fixable = False  # User must split the file
      self.solution = 'Split entity and architecture into seperate files.'

  def analyze(self, oFile):
      if oFile.hasEntity and oFile.hasArchitecture:
          self.add_violation(1)
