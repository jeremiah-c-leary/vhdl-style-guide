
from vsg.rules.whitespace import whitespace_rule

import re


class rule_006(whitespace_rule):
    '''Whitespace rule 006 checks for spaces after an open parenthesis.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove spaces before close ).'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.hasComment:
                sLine = oLine.line[:oLine.line.find('--')]
            else:
                sLine = oLine.line
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
