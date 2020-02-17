
from vsg import rule
from vsg import utils

import re


class rule_023(rule.rule):
    '''
    Instantiation rule 023 checks for comments after port and generic assignments.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '023'
        self.solution = 'Remove comment.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideInstantiation and oLine.hasComment:
            if oLine.isInstantiationPortAssignment or oLine.isInstantiationGenericAssignment:
                dViolation = utils.create_violation_dict(iLineNumber)
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub('\s*--.*', '', oLine.line))
            oLine.hasComment = False
            oLine.hasInlineComment = False
