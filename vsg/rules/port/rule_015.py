
from vsg.rules.port import port_rule


class rule_015(port_rule):
    '''
    Port rule 015 checks the indentation of closing parenthesis for port maps.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap and not oLine.isPortDeclaration:
                self._check_indent(oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
