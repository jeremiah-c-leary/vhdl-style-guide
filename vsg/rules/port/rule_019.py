
from vsg.rules.port import port_rule


class rule_019(port_rule):
    '''
    Port rule 019 checks the port direction is lowercase.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '019'
        self.solution = 'Change port direction to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                sLine = oLine.line.split(':')[1]
                self._is_lowercase(sLine.split()[0],iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            sLine = oFile.lines[iLineNumber].line.split(':')[1]
            self._lower_case(oFile.lines[iLineNumber], sLine.split()[0])
