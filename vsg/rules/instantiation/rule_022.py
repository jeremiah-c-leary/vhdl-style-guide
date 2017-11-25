
from vsg.rules.instantiation import instantiation_rule

import re


class rule_022(instantiation_rule):
    '''
    Instantiation rule 022 checks for a single space after the => operator.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '022'
        self.solution = 'Only a single space after => operator.'
        self.phase = 2

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment and not oLine.isInstantiationPortKeyword:
                if not re.match('^.*=>\s\S+', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], '=>')
