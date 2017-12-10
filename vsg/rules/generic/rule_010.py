
from vsg import rule
from vsg import line

import re


class rule_010(rule.rule):
    '''Generic rule 010 checks the closing parenthesis for generics are on a line by itself.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'
        self.identifier = '010'
        self.solution = 'Closing parenthesis must be on a line by itself.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap and not re.match('^\s*\)', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines[iLineNumber].line = re.sub(r'\)(\s*);', r' \1 ', oFile.lines[iLineNumber].line)
            oFile.lines[iLineNumber].isEndGenericMap = False
            oFile.lines.insert(iLineNumber + 1, line.line('  );'))
            oFile.lines[iLineNumber + 1].isEndGenericMap = True
            oFile.lines[iLineNumber + 1].insideGenericMap = True
            if oFile.lines[iLineNumber].isGenericKeyword:
                oFile.lines[iLineNumber + 1].indentLevel = oFile.lines[iLineNumber].indentLevel
            else:
                oFile.lines[iLineNumber + 1].indentLevel = oFile.lines[iLineNumber].indentLevel
                oFile.lines[iLineNumber].indentLevel = oFile.lines[iLineNumber].indentLevel + 1
