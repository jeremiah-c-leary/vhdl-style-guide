
from vsg.rules.library import library_rule
from vsg import check


class rule_008(library_rule):
    '''
    Library rule 008 checks indentation of the use keyword.
    '''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
