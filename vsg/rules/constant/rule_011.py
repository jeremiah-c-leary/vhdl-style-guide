
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_011(rule.rule):
    '''
    Constant rule 010 checks the constant type is lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'constant'
        self.identifier = '011'
        self.solution = 'Change constant type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if re.match('^\s*constant\s+.*:\s*\w', oLine.line, re.IGNORECASE):
                    sLine = oLine.line.split(':')[1].lstrip()
                    if '(' in sLine:
                        check.is_lowercase(self, sLine.split('(')[0].rstrip(), iLineNumber)
                    else:
                        check.is_lowercase(self, sLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split(':')[1].lstrip().split()[0]
            if '(' in sLine:
                fix.lower_case(self, oLine, sLine.split('(')[0].rstrip())
            else:
                fix.lower_case(self, oLine, sLine)
