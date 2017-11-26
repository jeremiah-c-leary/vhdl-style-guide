
from vsg.rules.port import port_rule
from vsg import line

import re


class rule_014(port_rule):
    '''
    Port rule 014 checks the closing parenthesis for ports are on a line by itself.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Closing parenthesis must be on a line by itself and above the "end" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap:
                if not re.match('^\s*\)', oLine.line):                 
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines[iLineNumber].update_line(re.sub(r'\)(\s*);', r' \1 ', oFile.lines[iLineNumber].line))
            oFile.lines[iLineNumber].isEndPortMap = False
            oFile.lines[iLineNumber].indentLevel += 1
            oFile.lines.insert(iLineNumber + 1, line.line('  );'))
            oFile.lines[iLineNumber + 1].isEndPortMap = True
            oFile.lines[iLineNumber + 1].insidePortMap = True
            oFile.lines[iLineNumber + 1].insideEntity = True
            oFile.lines[iLineNumber + 1].indentLevel = oFile.lines[iLineNumber].indentLevel - 1
