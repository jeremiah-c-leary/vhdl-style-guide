
from vsg import rule
from vsg import fix
from vsg import check


class rule_005(rule.rule):
    '''Case rule 005 checks for a single space before the "=>" keyword.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'case'
        self.identifier = '005'
        self.solution = 'Ensure a single space exists before the "=>" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenEnd:
                check.is_single_space_before(self, '=>', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_before_word(self, oFile.lines[iLineNumber], '=>')
