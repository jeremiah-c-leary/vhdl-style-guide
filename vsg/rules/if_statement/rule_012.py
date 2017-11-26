
from vsg.rules.if_statement import if_rule

import re


class rule_012(if_rule):
    '''If rule 012 checks for code after the "then" keyword.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Move code after "then" keyword to the next line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isThenKeyword:
                if re.match('^.*\sthen\s+\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._split_line_after_word(oFile, iLineNumber, ' then')
            oFile.lines[iLineNumber].isEndIfKeyword = False
            oFile.lines[iLineNumber].isElseKeyword = False
            oFile.lines[iLineNumber + 1].isThenKeyword = False
            oFile.lines[iLineNumber + 1].isIfKeyword = False
            oFile.lines[iLineNumber + 1].indentLevel += 1
