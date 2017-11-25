
from vsg.rules.instantiation import instantiation_rule


class rule_016(instantiation_rule):
    '''
    Instantiation rule 016 checks the generic name is uppercase.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Uppercase generic name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericAssignment and not oLine.isInstantiationGenericKeyword:
                self._is_uppercase(oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split('=>')
            self._upper_case(oFile.lines[iLineNumber], lLine[0].rstrip().lstrip())
