
from vsg.rules.instantiation import instantiation_rule

import re


class rule_003(instantiation_rule):
    '''
    Instantiation rule 003 checks for a single space before the :
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure only one space before the :.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                if not re.match('^\s*\S+\s:', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], ':')
