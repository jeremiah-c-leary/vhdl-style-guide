
from vsg.rules.package import package_rule

import re


class rule_013(package_rule):
    '''
    Package rule 013 checks the "is" keyword is lower case.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Change "is" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                if re.match('^\s*package\s+\w+\s+is', oLine.lineLower):
                    if not re.match('^\s*\w+\s+\w+\s+is', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'is')
