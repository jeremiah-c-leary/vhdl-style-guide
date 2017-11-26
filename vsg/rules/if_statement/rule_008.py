
from vsg.rules.if_statement import if_rule
from vsg import check


class rule_008(if_rule):
    '''If rule 008 checks for an empty line before the "end if" keyword.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Remove blank line(s) before the "end if" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndIfKeyword and not oFile.lines[iLineNumber - 2].isEndCaseKeyword and not oLine.isIfKeyword:
                check.is_no_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._remove_blank_lines_above(oFile, iLineNumber)
