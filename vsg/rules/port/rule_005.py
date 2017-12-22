
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_005(rule.rule):
    '''
    Port rule 005 checks for a single space after the colon in a port declaration for "in" and "inout" ports.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'port'
        self.identifier = '005'
        self.solution = 'Reduce number of spaces after the colon to 1.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and re.match('^.*:\s*in', oLine.line, re.IGNORECASE):
                check.is_single_space_after_character(self, ':', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_one_space_after_word(self, oLine, ':')
