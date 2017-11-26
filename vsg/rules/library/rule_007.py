
from vsg.rules.library import library_rule
from vsg import check


class rule_007(library_rule):
    '''
    Library rule 007 checks for a blank line above the "use" keyword.
    '''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove blank line(s) above "use" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                check.is_no_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._remove_blank_lines_above(oFile, iLineNumber)
