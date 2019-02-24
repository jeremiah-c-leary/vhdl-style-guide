
from vsg import rule
from vsg import fix

import re


class rule_030(rule.rule):
    '''
    Instantiation rule 030 checks for a single space after the => operator in generic maps.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '030'
        self.solution = 'Only a single space after => operator.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericAssignment and not oLine.isInstantiationGenericKeyword:
                if not re.match('^.*=>\s\S+', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], '=>')
