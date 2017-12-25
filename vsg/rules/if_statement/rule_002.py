
from vsg import rule

import re


class rule_002(rule.rule):
    '''
    If rule 002 checks the if boolean expression is enclosed in ()'s.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'if'
        self.identifier = '002'
        self.solution = 'Enclose boolean expression in ()\'s.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isIfKeyword and not re.match('^\s*if\s*\(', oLine.lineNoComment.lower()):
                    self.add_violation(iLineNumber)
            if oLine.isElseIfKeyword and re.match('^\s*elsif\s+\w', oLine.lineNoComment.lower()):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            if oLine.isIfKeyword:
                oLine.update_line(re.sub(r'^(\s*)[i|I][f|F]', r'\1if (', oLine.line))
            if oLine.isElseIfKeyword:
                oLine.update_line(re.sub('^(\s*)[e|E][l|L][s|S][i|I][f|F]', r'\1elsif (', oLine.line))
            iThenLineIndex = iLineNumber
            while not oLine.isThenKeyword:
                iThenLineIndex += 1
                oLine = oFile.lines[iThenLineIndex]
            oLine.update_line(re.sub('[t|T][h|H][e|E][n|N]', ') then', oLine.line))
