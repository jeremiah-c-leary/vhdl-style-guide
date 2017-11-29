
from vsg.rules.signal import signal_rule
from vsg import fix
from vsg import check

import re


class rule_010(signal_rule):
    '''
    Signal rule 010 checks the signal type is lowercase.
    '''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Change signal type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if re.match('^\s*signal\s+\w+\s+:\s+\w', oLine.lineLower):
                    sLine = oLine.line.split()[3]
                    if '(' in sLine:
                        check.is_lowercase(self, sLine.split('(')[0], iLineNumber)
                    else:
                        check.is_lowercase(self, oLine.line.split()[3], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split()[3]
            if '(' in sLine:
                fix.lower_case(self, oLine, sLine.split('(')[0])
            else:
                fix.lower_case(self, oLine, sLine)
