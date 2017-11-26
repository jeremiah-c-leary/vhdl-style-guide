
from vsg.rules.type import type_rule


class rule_002(type_rule):
    '''
    Type rule 002 checks the "type" keyword is lowercase.
    '''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lowercase "type" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'type')
