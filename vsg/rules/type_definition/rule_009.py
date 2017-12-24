
from vsg import rule
from vsg import utilities

import re


class rule_009(rule.rule):
    '''
    Type rule 009 checks for enumerated types after the open parenthesis on a multi-line type declaration.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'type', '009')
        self.solution = 'Move enumerated type to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeEnumeratedKeyword and not oLine.isTypeEnumeratedEnd:
                if re.match('^.*\sis\s*\(\s*\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utilities.split_line_after_word(oFile, iLineNumber, '(')
            oLine = oFile.lines[iLineNumber + 1]
            oLine.isTypeKeyword = False
            oLine.isTypeEnumeratedKeyword = False
            oLine.indentLevel += 1
