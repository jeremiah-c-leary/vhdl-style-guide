
from vsg.rules.package import package_rule
from vsg import fix
from vsg import check

import re


class rule_008(package_rule):
    '''
    Package rule 008 checks the package name is upper case on the closing "end package" line.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Uppercase package name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                if re.match('^\s*end\s+package\s+\w', oLine.lineLower):
                    lLine = oLine.line.split()
                    check.is_uppercase(self, lLine[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[2])
