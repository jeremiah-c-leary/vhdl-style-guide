
from vsg import rule
from vsg import check
from vsg import line


class rule_003(rule.rule):
    '''
    Entity rule 003 checks for a blank line above the entity keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'
        self.identifier = '003'
        self.solution = 'Add blank line above entity keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                check.is_blank_line_before(self, oFile, iLineNumber, None)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.insert(iLineNumber, line.blank_line())
