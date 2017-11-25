
from vsg.rules.entity import entity_rule


class rule_016(entity_rule):
    '''
    Entity rule 016 checks for a blank line above the "end entity" keywords.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Remove blank line(s) above "end entity" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                self._is_no_blank_line_before(oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._remove_blank_lines_above(oFile, iLineNumber)
