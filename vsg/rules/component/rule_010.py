
from vsg.rules.component import component_rule


class rule_010(component_rule):
    '''Component rule 010 checks the "end" keyword is lowercase.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Change "end" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                self._is_lowercase(oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'end')
