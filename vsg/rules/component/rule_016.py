
from vsg import rule
from vsg import fix
from vsg import check


class rule_016(rule.rule):
    '''
    Component rule 016 checks for a blank line above the "end component" keywords.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '016'
        self.solution = 'Remove blank line(s) above "end component" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                check.is_no_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.remove_blank_lines_above(self, oFile, iLineNumber)
