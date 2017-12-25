
from vsg import rule

import re


class rule_028(rule.rule):
    '''
    If rule 028 checks the **end if** keywords are lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'if', '028')
        self.phase = 6
        self.solution = 'lowercase "end if" keywords.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndIfKeyword and re.match('^\s*end\s+if', oLine.line, re.IGNORECASE):
                if not re.match('^\s*end\s+if', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('end\s+if', 'end if', oLine.line, 1, re.IGNORECASE))
