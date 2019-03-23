
from vsg import rule
from vsg import utils

import re


class rule_024(rule.rule):
    '''
    If rule 024 checks for code after the "then" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'if'
        self.identifier = '024'
        self.solution = 'Move code after "then" keyword to the next line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isThenKeyword and re.match('^.*[\s|)]then\s+\w', oLine.line, re.IGNORECASE):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utils.split_line_after_word(oFile, iLineNumber, 'then')
            oFile.lines[iLineNumber].isEndIfKeyword = False
            oFile.lines[iLineNumber].isElseKeyword = False
            oFile.lines[iLineNumber + 1].isThenKeyword = False
            oFile.lines[iLineNumber + 1].isIfKeyword = False
            oFile.lines[iLineNumber + 1].isElseIfKeyword = False
            oFile.lines[iLineNumber + 1].indentLevel += 1
            oFile.lines[iLineNumber].isLastEndIf = False
            utils.reclassify_line(oFile, iLineNumber)
            oFile.lines[iLineNumber + 1].isFirstIf = False
