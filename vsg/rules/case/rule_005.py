
from vsg.rules.case import case_rule


class rule_005(case_rule):
    '''Case rule 005 checks for a single space before the "=>" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure a single space exists before the "=>" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenEnd:
                self._is_single_space_before('=>', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], '=>')
