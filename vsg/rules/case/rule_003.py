
from vsg.rules.case import case_rule


class rule_003(case_rule):
    '''Case rule 003 checks for a single space before the "is" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure a single space exists before the "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseIsKeyword:
                self._is_single_space_before('is', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], 'is')
