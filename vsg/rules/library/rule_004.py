
from vsg.rules.library import library_rule


class rule_004(library_rule):
    '''
    Library rule 004 checks the library keyword is lower case.
    '''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change "library" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibrary:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'library')
