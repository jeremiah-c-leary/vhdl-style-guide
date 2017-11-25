
from vsg.rules.instantiation import instantiation_rule


class rule_008(instantiation_rule):
    '''
    Instantiation rule 008 checks the instance name is uppercase in the instantiation declaration line.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change instance name to all uppercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                self._is_uppercase(oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[0])
