
from vsg import rule
from vsg import fix
from vsg import check


class rule_013(rule.rule):
    '''
    Component rule 013 checks for a single space after the "component"
    keyword in the closing of the component.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '013'
        self.solution = 'Reduce spaces after "component" keyword to one.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd and len(oLine.line.split()) >= 3:
                check.is_single_space_after(self, 'component', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_one_space_after_word(self, oLine, 'component')
