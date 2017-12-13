
from vsg import rule
from vsg import utilities

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

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isThenKeyword and re.match('^.*\sthen\s+\w', oLine.line, re.IGNORECASE):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utilities.split_line_after_word(oFile, iLineNumber, ' then')
            oFile.lines[iLineNumber].isEndIfKeyword = False
            oFile.lines[iLineNumber].isElseKeyword = False
            oFile.lines[iLineNumber + 1].isThenKeyword = False
            oFile.lines[iLineNumber + 1].isIfKeyword = False
            oFile.lines[iLineNumber + 1].indentLevel += 1
            if re.match('^\s*return', oFile.lines[iLineNumber + 1].line, re.IGNORECASE):
                oFile.lines[iLineNumber].isFunctionReturn = False
                oFile.lines[iLineNumber + 1].isFunctionReturn = True
            elif re.match('^\s*\w+.*:=', oFile.lines[iLineNumber + 1].line, re.IGNORECASE):
                oFile.lines[iLineNumber + 1].insideVariableAssignment = True
                oFile.lines[iLineNumber + 1].isVariableAssignmentEnd = True
                oFile.lines[iLineNumber + 1].isVariableAssignment = True
            else: 
                oFile.lines[iLineNumber + 1].insideSequential = True
                oFile.lines[iLineNumber + 1].isSequentialEnd = True
                oFile.lines[iLineNumber + 1].isSequential = True
