
from vsg.rules.component import component_rule
from vsg import fix
from vsg import check


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
                check.is_lowercase(self, oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'component')
