
from vsg import rule
from vsg import fix

import re


class rule_022(rule.rule):
    '''
    Instantiation rule 022 checks for a single space after the => operator.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '022'
        self.solution = 'Only a single space after => operator.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment and not oLine.isInstantiationPortKeyword:
                if not re.match('^.*=>\s\S+', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], '=>')
