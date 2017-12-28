
from vsg import rule
from vsg import fix

import re


class rule_009(rule.rule):
    '''
    Package rule 009 checks for a single space between the "end" and "package" keywords and component name.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'package', '009')
        self.solution = 'Single space between "end" and "package" keywords and component name.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageEnd:
                check_spaces_between_end_and_package_and_name(self, oLine, iLineNumber)
                check_spaces_between_end_and_package(self, oLine, iLineNumber)
                check_spaces_between_end_and_name(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'end')
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'package')


def check_spaces_between_end_and_package_and_name(self, oLine, iLineNumber):
    if re.match('^\s*end\s+package\s+\w', oLine.lineLower):
        if not re.match('^\s*end\spackage\s\w', oLine.lineLower):
            self.add_violation(iLineNumber)


def check_spaces_between_end_and_package(self, oLine, iLineNumber):
    if re.match('^\s*end\s+package', oLine.lineLower):
        if not re.match('^\s*end\spackage', oLine.lineLower):
            self.add_violation(iLineNumber)


def check_spaces_between_end_and_name(self, oLine, iLineNumber):
    if re.match('^\s*end\s+\w', oLine.lineLower):
        if not re.match('^\s*end\s\w', oLine.lineLower):
            self.add_violation(iLineNumber)
