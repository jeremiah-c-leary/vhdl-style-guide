
from vsg.rules.process import process_rule

import re


class rule_017(process_rule):
    '''
    Process rule 017 checks the process label is uppercase.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Uppercase process label.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if re.match('^\s*\S+\s*:', oLine.line):
                    lLine = oLine.line.split(':')
                    if not lLine[0] == lLine[0].upper():
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split(':')
            self._upper_case(oFile.lines[iLineNumber], lLine[0].rstrip().lstrip())
