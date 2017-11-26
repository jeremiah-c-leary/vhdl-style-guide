
from vsg.rules.package import package_rule

import re


class rule_006(package_rule):
    '''
    Package rule 006 checks for the "end" and "package" keyword are lower case.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure "end" and "package" keywords are lower case.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                if re.match('^\s*end\s+package', oLine.lineLower):
                    if not re.match('^\s*end\s+package', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'end')
            self._lower_case(oFile.lines[iLineNumber], 'package')
