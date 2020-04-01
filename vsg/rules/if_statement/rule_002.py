
from vsg import rule
from vsg import utils

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

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isIfKeyword and not re.match('^\s*if\s*\(', oLine.lineNoComment.lower()):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)
        if oLine.isElseIfKeyword and re.match('^\s*elsif\s+\w', oLine.lineNoComment.lower()):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = utils.get_violation_linenumber(dViolation)
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
