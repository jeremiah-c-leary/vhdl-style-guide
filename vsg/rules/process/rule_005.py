
from vsg.rules.process import process_rule

import re


class rule_005(process_rule):
    '''
    Process rule 004 checks the "process" keyword is lower case.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Lowercase the "process" keyword.' 
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if not re.match('^\s*.*process', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'process')
