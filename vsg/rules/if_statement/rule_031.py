
from vsg import rule
from vsg import check
from vsg import fix


class rule_031(rule.rule):
    '''
    If rule 031 checks for a blank line before the "end if" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'if', '031')
        self.phase = 3
        self.solution = 'Add a blank line before the "if"'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFirstIf:
                check.is_blank_line_before(self, oFile, iLineNumber, 'isComment')

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.insert_blank_line_above(self, oFile, iLineNumber)
