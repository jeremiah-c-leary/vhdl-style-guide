
from vsg import rule
from vsg import fix

import re


class rule_006(rule.rule):
    '''
    Package rule 006 checks for the "end" and "package" keyword are lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'package'
        self.identifier = '006'
        self.solution = 'Ensure "end" and "package" keywords are lower case.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd and re.match('^\s*end\s+package', oLine.lineLower):
                if not re.match('^\s*end\s+package', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'end')
            fix.lower_case(self, oFile.lines[iLineNumber], 'package')
