
from vsg.rules.package import package_rule

import re


class rule_002(package_rule):
    '''
    Package rule 002 checks for a single space between "package" and "is" keywords.
    '''

    def __init__(self):
        package_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces between keywords.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                if len(oLine.line.split()) > 2:
                    if re.match('^\s*package\s+\S+\s+is', oLine.lineLower):
                        if not re.match('^\s*package\s\S+\sis', oLine.lineLower):
                            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'package')
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], 'is')
