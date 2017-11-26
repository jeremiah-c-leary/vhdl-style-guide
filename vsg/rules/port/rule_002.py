
from vsg.rules.port import port_rule
from vsg import check


class rule_002(port_rule):
    '''
    Port rule 002 checks indentation of the "port" keyword.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
