
from vsg import rule
from vsg import utils

import re


class rule_007(rule.rule):
    '''
    Package rule 007 checks for the "package" keyword on the end package declaration.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'package'
        self.identifier = '007'
        self.solution = 'End of package follows this format: end package <package name>.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPackageEnd and not re.match('^\s*end\s+package', oLine.lineLower):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            iIndex = oLine.lineLower.find('end') + len('end')
            oLine.update_line(oLine.line[:iIndex] + ' package' + oLine.line[iIndex:])
