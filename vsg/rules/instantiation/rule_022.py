
from vsg import rule
from vsg import fix
from vsg import utils

import re


class rule_022(rule.rule):
    '''
    Instantiation rule 022 checks for a single space after the => operator in port maps.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '022'
        self.solution = 'Only a single space after => operator.'
        self.phase = 2

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationPortAssignment and not oLine.isInstantiationPortKeyword:
            if not re.match('^.*=>\s\S+', oLine.line):
                dViolation = utils.create_violation_dict(iLineNumber)
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = dViolation['lineNumber']
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], '=>')
