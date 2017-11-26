
from vsg.rules.package import package_rule

import re


class rule_004(package_rule):
    '''
    Package rule 004 checks the package keyword is lower case.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change package keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                if not re.match('^\s*package', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'package')
