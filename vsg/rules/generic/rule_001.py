
from vsg.rules.generic import generic_rule
from vsg import check


class rule_001(generic_rule):
    '''Generic rule 001 checks for a blank line above the "generic" keyword.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove blank lines above "generic" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                check.is_no_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            while oFile.lines[iLineNumber - 1].isBlank:
                oFile.lines.pop(iLineNumber - 1)
