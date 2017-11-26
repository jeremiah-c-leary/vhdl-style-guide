
from vsg.rules.component import component_rule


class rule_008(component_rule):
    '''Component rule 008 checks the component name is uppercase in the component declaration line.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change component name to all uppercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                self._is_uppercase(oLine.line.split()[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split()
            self._upper_case(oFile.lines[iLineNumber], lLine[1])
