
from vsg.rules.instantiation import instantiation_rule
from vsg import check


class rule_001(instantiation_rule):
    '''
    Instantiation rule 001 checks for proper indent of instantiations.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration or oLine.isInstantiationPortAssignment or oLine.isInstantiationPortEnd or oLine.isInstantiationPortKeyword or oLine.isInstantiationGenericAssignment or oLine.isInstantiationGenericEnd or oLine.isInstantiationGenericKeyword:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
