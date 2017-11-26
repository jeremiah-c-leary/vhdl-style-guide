
from vsg.rules.if_statement import if_rule

import re


class rule_016(if_rule):
    '''If rule 016 checks for code after the "else" keyword.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Move code after "else" keyword to the next line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isElseKeyword:
                if re.match('^.*\selse\s+\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._split_line_after_word(oFile, iLineNumber, ' else')
            oFile.lines[iLineNumber + 1].isElseKeyword = False
            oFile.lines[iLineNumber].isIfKeyword = False
            oFile.lines[iLineNumber].isElseIfKeyword = False
            oFile.lines[iLineNumber].isThenKeyword = False
            oFile.lines[iLineNumber + 1].indentLevel += 1
