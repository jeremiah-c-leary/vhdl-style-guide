
from vsg import rule
from vsg import check
from vsg import fix


class rule_001(rule.rule):
    '''
    Instantiation rule 001 checks for proper indent of instantiations.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration or oLine.isInstantiationPortAssignment or \
               oLine.isInstantiationPortEnd or oLine.isInstantiationPortKeyword or \
               oLine.isInstantiationGenericAssignment or oLine.isInstantiationGenericEnd or \
               oLine.isInstantiationGenericKeyword:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])
