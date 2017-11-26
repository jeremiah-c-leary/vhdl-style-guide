
from vsg.rules.if_statement import if_rule

import re


class rule_002(if_rule):
    '''If rule 002 checks the if boolean expression is enclosed in ()'s.'''

    def __init__(self):
        if_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Enclose boolean expression in ()\'s.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isIfKeyword:
                if not re.match('^\s*if\s*\(', oLine.lineLower):
                    self.add_violation(iLineNumber)
            if oLine.isElseIfKeyword:
                if re.match('^\s*elsif\s+\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            if oLine.isIfKeyword:
                oLine.update_line(oLine.line.replace('if', 'if ('))
            if oLine.isElseIfKeyword:
                oLine.update_line(oLine.line.replace('elsif', 'elsif ('))
            iThenLineIndex = iLineNumber
            while not oLine.isThenKeyword:
                iThenLineIndex += 1
                oLine = oFile.lines[iThenLineIndex]
            oLine.update_line(oLine.line.replace('then', ') then'))
