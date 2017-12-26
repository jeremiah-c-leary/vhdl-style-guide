
from vsg import rule
from vsg import fix
from vsg import check


class rule_008(rule.rule):
    '''If rule 008 checks for an empty line before the "end if" keyword.'''

    def __init__(self):
        rule.rule.__init__(self, 'if', '008')
        self.solution = 'Remove blank line(s) before the "end if" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndIfKeyword and not oLine.isIfKeyword:
                check.is_no_blank_line_before(self, oFile, iLineNumber, 'isEndCaseKeyword')

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.remove_blank_lines_above(self, oFile, iLineNumber, 'isEndCaseKeyword')
