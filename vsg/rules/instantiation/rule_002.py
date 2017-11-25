
from vsg.rules.instantiation import instantiation_rule

import re


class rule_002(instantiation_rule):
    '''
    Instantiation rule 002 checks for a single space after the :
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure only one space after the :.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                if not re.match('^\s*\S+\s*:\s\S', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':')
