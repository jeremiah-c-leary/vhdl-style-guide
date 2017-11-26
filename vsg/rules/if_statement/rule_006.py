
from vsg.rules.if_statement import if_rule
from vsg import check


class rule_006(if_rule):
    '''If rule 006 checks for an empty line after the then keyword.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove blank line(s) after the "then" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isThenKeyword and not oFile.lines[iLineNumber + 2].isCaseKeyword and not oLine.isEndIfKeyword:
                check.is_no_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._remove_blank_lines_below(oFile, iLineNumber)
