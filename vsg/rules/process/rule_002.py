
from vsg import rule
from vsg import fix
from vsg import utils

import re


class rule_002(rule.rule):
    '''
    Process rule 002 checks there is a single space between the process
    keyword and the (.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'process'
        self.identifier = '002'
        self.solution = 'Ensure a single space exists between the "process" \
                          keyword and the (.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isProcessKeyword and re.match('^\s*.*process\s*\(', oLine.lineLower) and not re.match('^\s*.*process\s\(', oLine.lineLower):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            fix.enforce_one_space_after_word(self, utils.get_violating_line(oFile, dViolation), 'process')
