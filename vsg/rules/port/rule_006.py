
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_006(rule.rule):
    '''
    Port rule 006 checks for one space after the colon in a port declaration for "out" ports.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'port'
        self.identifier = '006'
        self.solution = 'Change number of spaces before "out" to 3.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration and re.match('^\s*\S+\s*:\s*out', oLine.lineLower):
                check.is_single_space_before(self, 'out', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_one_space_before_word(self, oLine, 'out')
