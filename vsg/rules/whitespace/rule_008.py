
from vsg import rule

import re


class rule_008(rule.rule):
    '''
    Whitespace rule 008 checks for spaces after "std_logic_vector"
    '''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '008')
        self.phase = 2
        self.solution = 'Remove spaces after "std_logic_vector".'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if re.match('^.*std_logic_vector\s+\(', oLine.line, re.IGNORECASE):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'([r|R])\s+\(', r'\1(', oLine.line, 1, re.IGNORECASE))
