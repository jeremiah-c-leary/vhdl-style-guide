
from vsg.rules.process import process_rule

import re


class rule_019(process_rule):
    '''
    Process rule 019 checks the "end process" label is uppercase.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '019'
        self.solution = 'Uppercase the label.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if re.match('^\s*\w+\s+\w+\s+\w+', oLine.line):
                    self._is_uppercase(oLine.line.split()[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split()
            self._upper_case(oFile.lines[iLineNumber], lLine[2])
