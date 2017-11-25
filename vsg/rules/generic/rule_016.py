
from vsg.rules.generic import generic_rule

import re


class rule_016(generic_rule):
    '''Generic rule 016 checks for multiple generate terms on a single line.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Move multiple generates to their own lines.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\w+\s*:.*;\s*\w+\s*:', oLine.line):
                    self.add_violation(iLineNumber)
