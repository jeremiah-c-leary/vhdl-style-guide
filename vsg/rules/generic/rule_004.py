
from vsg.rules.generic import generic_rule
from vsg import check


class rule_004(generic_rule):
    '''Generic rule 004 checks indentation of generics.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration and not oLine.isEndGenericMap:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
