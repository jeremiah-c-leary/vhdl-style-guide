
from vsg.rules.port import port_rule
from vsg import check


class rule_004(port_rule):
    '''
    Port rule 004 checks indentation of ports.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and not oLine.isEndPortMap:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
