
from vsg.rules.port import port_rule


class rule_010(port_rule):
    '''
    Port rule 010 checks port names are uppercase.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Uppercase port name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                self._is_uppercase(self._get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[0])
