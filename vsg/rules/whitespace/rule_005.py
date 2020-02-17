
from vsg import rule
from vsg import utils

import re


class rule_005(rule.rule):
    '''Whitespace rule 005 checks for spaces after an open parenthesis.'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '005')
        self.phase = 2
        self.solution = 'Remove spaces after open (.'

    def _analyze(self, oFile, oLine, iLineNumber):
        sLine = oLine.lineNoComment
        if re.match('^.*\(\s+', sLine) and not re.match('^.*\(\s+[0-9]', sLine):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            iCommentIndex = oLine.line.find('--')
            if iCommentIndex == -1:
                oLine.update_line(re.sub(r'\((\s+)([A-Za-z_\(])', r'(\2', oLine.line))
            else:
                sLine = oLine.line[:iCommentIndex]
                sLine = re.sub(r'\((\s+)([A-Za-z_\(])', r'(\2', sLine)
                sLine = sLine + oLine.line[iCommentIndex:]
                oLine.update_line(sLine)
