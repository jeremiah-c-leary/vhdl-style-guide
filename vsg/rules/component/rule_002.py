
from vsg import rule
from vsg import fix

import re


class rule_002(rule.rule):
    '''
    Component rule 002 checks for a single space after the "component" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '002'
        self.solution = 'Remove extra spaces after "component" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                if re.match('^\s*component\s\s+\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'component')
