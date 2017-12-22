
from vsg import rule

import re


class rule_006(rule.rule):
    '''Whitespace rule 006 checks for spaces before a close parenthesis.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'whitespace'
        self.identifier = '006'
        self.phase = 2
        self.solution = 'Remove spaces before close ).'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            sLine = oLine.lineNoComment
            if re.match('^.*\s+\)', sLine) and not re.match('^\s+\)', sLine):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iCommentIndex = oLine.line.find('--')
            if iCommentIndex == -1:
                oLine.update_line(re.sub(r'\s+\)', r')', oLine.line))
            else:
                sLine = oLine.line[:iCommentIndex]
                sLine = re.sub(r'\s+\)', r')', sLine)
                sLine = sLine + oLine.line[iCommentIndex:]
                oLine.update_line(sLine)
