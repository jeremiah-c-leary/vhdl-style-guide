
from vsg import rule
from vsg import fix
from vsg import check


class rule_014(rule.rule):
    '''
    Component rule 014 checks the "component" keyword is lower case in the
    closing of the component.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '014'
        self.solution = 'Change "component" keyword to lower case.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lLine = oLine.line.split()
                check.is_lowercase(self, lLine[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'component')
