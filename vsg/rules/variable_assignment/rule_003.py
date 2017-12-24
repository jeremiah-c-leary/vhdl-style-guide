
from vsg import rule
from vsg import check
from vsg import fix


class rule_003(rule.rule):
    '''Variable assignment rule 003 checks for a single space before the ":=" keyword.'''

    def __init__(self):
        rule.rule.__init__(self, 'variable_assignment', '003')
        self.solution = 'Ensure a single space exists before the ":=" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment:
                check.is_single_space_before_character(self, ':=', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_before_word(self, oFile.lines[iLineNumber], ':=')
