
from vsg.rules.component import component_rule


class rule_004(component_rule):
    '''
    Component rule 004 checks the component keyword is lower case.
    '''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change "component" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                self._is_lowercase(oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'component')
