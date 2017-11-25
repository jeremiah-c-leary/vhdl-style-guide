
from vsg.rules.generic import generic_rule
from vsg import line

import re

class rule_010(generic_rule):
    '''Generic rule 010 checks the closing parenthesis for generics are on a line by itself.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Closing parenthesis must be on a line by itself.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap:
                if not re.match('^\s*\)', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines[iLineNumber].line = re.sub(r'\)(\s*);', r' \1 ', oFile.lines[iLineNumber].line)
            oFile.lines[iLineNumber].isEndGenericMap = False
            oFile.lines[iLineNumber].indentLevel += 1
            oFile.lines.insert(iLineNumber + 1, line.line('  );'))
            oFile.lines[iLineNumber + 1].isEndGenericMap = True
            oFile.lines[iLineNumber + 1].insideGenericMap = True
            oFile.lines[iLineNumber + 1].indentLevel = oFile.lines[iLineNumber].indentLevel - 1
