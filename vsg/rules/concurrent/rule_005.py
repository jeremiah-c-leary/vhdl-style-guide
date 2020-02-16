
from vsg import rule
from vsg import utils

import re


class rule_005(rule.rule):
    '''
    Concurrent rule 005 checks for labels on concurrent assignments.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'
        self.identifier = '005'
        self.solution = 'Remove label on concurrent assignment.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isConcurrentBegin and re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(oLine.line[oLine.line.find(':') + 1:])
