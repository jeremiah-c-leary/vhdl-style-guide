
from vsg.rules.port import port_rule


class rule_018(port_rule):
    '''
    Port rule 018 checks the port type is lowercase.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Change port type to lowercase.'
        self.phase = 6
        self.fixable = False

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                sLine = oLine.line.split(':')[1]
                if '(' in sLine:
                    sLine = sLine.split('(')[0]
                    self._is_lowercase(sLine, iLineNumber)
                else:
                    self._is_lowercase(sLine.split()[1],iLineNumber)
