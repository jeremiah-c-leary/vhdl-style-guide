
from vsg.rules.variable import variable_rule

import re


class rule_010(variable_rule):
    '''
    Signal rule 010 checks the variable type is lowercase.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Change variable type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if re.match('^\s*variable\s+.*:\s*\w', oLine.lineLower):
                    sLine = oLine.line.split(':')[1].lstrip().rstrip().replace(';', '')
                    if '(' in sLine:
                        self._is_lowercase(sLine.split('(')[0], iLineNumber)
                    else:
                        self._is_lowercase(sLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split(':')[1].lstrip().rstrip().replace(';', '')
            if '(' in sLine:
                self._lower_case(oFile.lines[iLineNumber], sLine.split('(')[0])
            else:
                self._lower_case(oFile.lines[iLineNumber], sLine)
