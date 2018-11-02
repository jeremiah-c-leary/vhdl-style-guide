
from vsg import rule

import re


class rule_010(rule.rule):
    '''Whitespace rule 010 checks for spaces after the concat operator.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'
        self.identifier = '010'
        self.phase = 2
        self.solution = 'Add space after concat operator.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            sLine = oLine.lineNoComment
            if re.match('^.*&\w+', sLine):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iCommentIndex = oLine.line.find('--')
            if iCommentIndex == -1:
                oLine.update_line(re.sub(r'&(\w+)', r'& \1', oLine.line))
            else:
                sLine = oLine.line[:iCommentIndex]
                sLine = re.sub(r'&(\w+)', r'& \1', sLine)
                sLine = sLine + oLine.line[iCommentIndex:]
                oLine.update_line(sLine)
