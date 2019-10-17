
from vsg import rule
from vsg import fix

import re


class rule_009(rule.rule):
    '''Architecture rule 009 checks for the "end" and "architecture" keyword are lower case.'''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '009')
        self.solution = 'Ensure "end" and "architecture" keywords are lower case.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isEndArchitecture and \
           re.match('^\s*end\s\s*architecture', oLine.lineLower) and \
           not re.match('^\s*end\s\s*architecture', oLine.line):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(oFile.lines[iLineNumber], 'end')
            fix.lower_case(oFile.lines[iLineNumber], 'architecture')
