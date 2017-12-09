
from vsg import rule
from vsg import fix

import re


class rule_006(rule.rule):
    '''Generic rule 006 checks for a single space after the default assignment in a generic declaration.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'
        self.identifier = '006'
        self.solution = 'Reduce number of spaces after the default assignment to 1.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\S+\s*:\s*\S+\s*:=', oLine.line):
                    if not re.match('^\s*\S+\s*:\s*\S+\s*:=\s[\S\'"]', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], ':=')
