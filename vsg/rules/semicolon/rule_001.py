
import re

from vsg import rule
from vsg import utils

reMultipleSemiColons = re.compile('(.*);;+')


class rule_001(rule.rule):
    '''
    Checks for consecutive semicolons.

    '''
    def __init__(self):
        rule.rule.__init__(self, 'semicolon', '001')
        self.phase = 1
        self.solution = 'Remove consecutive semicolons.'

    def _analyze(self, oFile, oLine, iLineNumber):
        lStrings = utils.split_line_on_comment(oLine.line)
        if reMultipleSemiColons.match(lStrings[0]) is not None:
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            lStrings = utils.split_line_on_comment(oLine.line)
            sNewLine = utils.remove_consecutive_characters(lStrings[0], ';') + lStrings[1]
            oLine.update_line(sNewLine)
