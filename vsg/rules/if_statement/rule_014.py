
from vsg.rules.if_statement import if_rule

import re


class rule_014(if_rule):
    '''If rule 014 checks the "end if" keyword is on it's own line.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Move "end if" keyword to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndIfKeyword:
                if not re.match('^\s*end\s+if', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._split_line_before_word(oFile, iLineNumber, ' end')
            oFile.lines[iLineNumber].isEndIfKeyword = False
            oFile.lines[iLineNumber + 1].isIfKeyword = False
            oFile.lines[iLineNumber + 1].isElseIfKeyword = False
            oFile.lines[iLineNumber + 1].isElseKeyword = False
            oFile.lines[iLineNumber + 1].isThenKeyword = False
            oFile.lines[iLineNumber + 1].indentLevel -= 1
