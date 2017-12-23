
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_010(rule.rule):
    '''
    Signal rule 010 checks the variable type is lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'variable', '010')
        self.solution = 'Change variable type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if re.match('^\s*variable\s+.*:\s*\w', oLine.lineLower):
                    sLine = oLine.line.split(':')[1].lstrip().rstrip().replace(';', '')
                    if '(' in sLine:
                        check.is_lowercase(self, sLine.split('(')[0], iLineNumber)
                    else:
                        check.is_lowercase(self, sLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split(':')[1].lstrip().rstrip().replace(';', '')
            if '(' in sLine:
                fix.lower_case(self, oFile.lines[iLineNumber], sLine.split('(')[0])
            else:
                fix.lower_case(self, oFile.lines[iLineNumber], sLine)
