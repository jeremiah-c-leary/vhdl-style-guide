
from vsg.rules.package import package_rule

import re


class rule_007(package_rule):
    '''
    Package rule 007 checks for the "package" keyword on the end package declaration.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'End of package follows this format: end package <package name>.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                if not re.match('^\s*end\s+package', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iIndex = oLine.lineLower.find('end') + len('end')
            oLine.update_line(oLine.line[:iIndex] + ' package' + oLine.line[iIndex:])
