
from vsg import rule
from vsg import utils

import re


class rule_010(rule.rule):
    '''Whitespace rule 010 checks for spaces before and/or after the concat operator.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'
        self.identifier = '010'
        self.phase = 2
        self.solution = 'Add space before and/or after concat operator.'

    def _analyze(self, oFile, oLine, iLineNumber):
        sLine = oLine.lineNoComment
        if re.match('^.*&\w+', sLine) or re.match('^.*\w&', sLine):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            iCommentIndex = oLine.line.find('--')
            if iCommentIndex == -1:
                oLine.update_line(re.sub(r'&(\w+)', r'& \1', oLine.line))
                oLine.update_line(re.sub(r'(\w+)&', r'\1 &', oLine.line))
            else:
                sLine = oLine.line[:iCommentIndex]
                sLine = re.sub(r'&(\w+)', r'& \1', sLine)
                sLine = re.sub(r'(\w+)&', r'\1 &', sLine)
                sLine = sLine + oLine.line[iCommentIndex:]
                oLine.update_line(sLine)
