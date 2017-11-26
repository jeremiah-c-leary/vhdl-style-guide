
from vsg.rules.generic import generic_rule
from vsg import check


class rule_008(generic_rule):
    '''
    Generic rule 008 checks the indentation of closing parenthesis for generic maps.
    '''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap and not oLine.isGenericDeclaration:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
