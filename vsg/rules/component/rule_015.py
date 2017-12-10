
from vsg import rule

import re


class rule_015(rule.rule):
    '''
    Component rule 015 checks for the "component" keyword in the "end component" statement.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '015'
        self.solution = 'Add "component" keyword'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd and not re.match('^\s*end\s+component', oLine.line, re.IGNORECASE):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            lLine = oLine.line.split()
            if not lLine[1].lower() == 'component':
                lLine.insert(1, 'component')
                oLine.update_line(' '.join(lLine))
