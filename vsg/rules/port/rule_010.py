
from vsg.rules.port import port_rule
from vsg import utilities
from vsg import fix
from vsg import check


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
                check.is_uppercase(self, utilities.get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[0])
