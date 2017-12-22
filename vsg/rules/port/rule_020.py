
from vsg import rule

import re


class rule_020(rule.rule):
    '''
    Port rule 020 checks there is at least one space before the :.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '020')
        self.solution = 'Add a space before the :.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and not re.match('^.*\s+:', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.replace(':', ' :'))
