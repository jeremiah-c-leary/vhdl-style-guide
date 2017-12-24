
from vsg import rule
from vsg import check
from vsg import fix


class rule_002(rule.rule):
    '''
    Concurrent rule 002 checks there is a single space after the assignment.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'
        self.identifier = '002'
        self.solution = 'Remove all but one space after the <=.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                check.is_single_space_after_character(self, '<=', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], '<=')
