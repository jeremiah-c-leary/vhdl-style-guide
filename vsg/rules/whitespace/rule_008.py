
from vsg import rule
from vsg import utils

import re


class rule_008(rule.rule):
    '''
    Whitespace rule 008 checks for spaces after "std_logic_vector"
    '''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '008')
        self.phase = 2
        self.solution = 'Remove spaces after "std_logic_vector".'

    def _analyze(self, oFile, oLine, iLineNumber):
        if re.match('^.*std_logic_vector\s+\(', oLine.line, re.IGNORECASE):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub(r'([r|R])\s+\(', r'\1(', oLine.line, 1, re.IGNORECASE))
