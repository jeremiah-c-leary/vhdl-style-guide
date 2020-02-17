
import re

from vsg import rule
from vsg import utils


class rule_003(rule.rule):
    '''
    After rule 003 checks for the "after" keyword in signal assignments in reset portion of a clock process.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'after', '003')
        self.phase = 1
        self.disable = True
        self.solution = 'Remove after from signal in the reset portion of a clock process'

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideResetProcess and oLine.hasAfterKeyword:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            sNewLine = re.sub('\s*after.*;', ';', oLine.line, 1, flags=re.IGNORECASE)
            oLine.update_line(sNewLine)
            oLine.hasAfterKeyword = False
