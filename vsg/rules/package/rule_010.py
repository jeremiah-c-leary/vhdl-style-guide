
from vsg.rules.package import package_rule

import re


class rule_010(package_rule):
    '''
    Package rule 010 checks the package name is upper case in the package declaration.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Upper case package name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                if re.match('^\s*package\s+\w+', oLine.lineLower):
                    lLine = oLine.line.split()
                    self._is_uppercase(lLine[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])
