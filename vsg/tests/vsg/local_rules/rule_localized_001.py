
from vsg import rule
from vsg import token
from vsg import violation


class rule_001(rule.Rule):

  def __init__(self):
      rule.Rule.__init__(self, 'localized', '001')
      self.phase = 1
      self.fixable = False  # User must split the file
      self.solution = 'Split entity and architecture into seperate files.'

  def analyze(self, oFile):
      lToiEntity = oFile.get_tokens_matching([token.entity_declaration.entity_keyword])
      lToiArchitecture = oFile.get_tokens_matching([token.architecture_body.architecture_keyword])

      if len(lToiEntity) > 0 and len(lToiArchitecture) > 0:
          oViolation = violation.New(1, lToiEntity, self.solution)
          self.add_violation(oViolation)
