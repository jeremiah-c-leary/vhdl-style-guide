
from vsg import rule
from vsg import utils

import re


class rule_030(rule.rule):
    '''
    Process rule 030 checks for single signal declarations on sensitivity list lines.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'process'
        self.identifier = '030'
        self.solution = 'Compact sensitivity list to reduce the number of lines it uses.'
        self.phase = 1
        self.fixable = False

    def _pre_analyze(self):
        self.iCount = 0
        self.sSensitivityList = ''

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideSensitivityList:
            self.sSensitivityList += oLine.lineNoComment
            if not re.match('^\s*\)', oLine.lineNoComment):
                self.iCount += 1
        if oLine.isSensitivityListEnd:
            if self.iCount == self.sSensitivityList.count(',') + 1:
                if self.iCount > 1:
                    dViolation = utils.create_violation_dict(iLineNumber)
                    self.add_violation(dViolation)
            self.iCount = 0
            self.sSensitivityList = ''
