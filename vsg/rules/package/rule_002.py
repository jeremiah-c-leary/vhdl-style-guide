
from vsg import rule
from vsg import fix
from vsg import utils

import re


class rule_002(rule.rule):
    '''
    Package rule 002 checks for a single space between "package" and "is" keywords.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'package'
        self.identifier = '002'
        self.solution = 'Remove extra spaces between keywords.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPackageKeyword:
            if len(oLine.line.split()) > 2:
                if re.match('^\s*package\s+\S+\s+is', oLine.lineLower):
                    if not re.match('^\s*package\s\S+\sis', oLine.lineLower):
                        dViolation = utils.create_violation_dict(iLineNumber)
                        self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = utils.get_violation_line_number(dViolation)
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'package')
            fix.enforce_one_space_before_word(self, oFile.lines[iLineNumber], 'is')
