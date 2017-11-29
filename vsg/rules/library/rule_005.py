
from vsg.rules.library import library_rule
from vsg import fix
from vsg import check


class rule_005(library_rule):
    '''
    Library rule 005 checks the use keyword is lower case.
    '''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Change "use" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                check.is_lowercase(self, self._get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'use')
