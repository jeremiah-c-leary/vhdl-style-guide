
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_006(rule.rule):
    '''
    Port rule 006 checks for one space after the colon in a port declaration for "out" ports.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '006')
        self.solution = 'Change number of spaces after : to a single space.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and re.match('^.*:\s*out', oLine.line, re.IGNORECASE):
                check.is_single_space_after_character(self, ':', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_one_space_after_word(self, oLine, ':')
