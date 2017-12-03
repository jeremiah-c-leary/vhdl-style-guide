
from vsg import rule
from vsg import fix
from vsg import check


class rule_007(rule.rule):
    '''
    Library rule 007 checks for a blank line above the "use" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'library'
        self.identifier = '007'
        self.solution = 'Remove blank line(s) above "use" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                check.is_no_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.remove_blank_lines_above(self, oFile, iLineNumber)
