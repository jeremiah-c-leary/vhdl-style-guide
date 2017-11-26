
from vsg.rules.component import component_rule


class rule_012(component_rule):
    '''Component rule 012 checks component name is uppercase in "end" keyword line.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Uppercase component name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    self._is_uppercase(lLine[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split()
            self._upper_case(oFile.lines[iLineNumber], lLine[2])
