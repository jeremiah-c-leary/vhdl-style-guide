
from vsg import rule
from vsg import check
from vsg import fix


class rule_030(rule.rule):
    '''
    If rule 030 checks for a blank line after the "end if" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'if', '030')
        self.phase = 3
        self.solution = 'Add a blank line after the "end if"'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLastEndIf:
                check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.insert_blank_line_below(self, oFile, iLineNumber)
