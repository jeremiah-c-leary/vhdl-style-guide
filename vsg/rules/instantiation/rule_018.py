
from vsg.rules.instantiation import instantiation_rule

import re


class rule_018(instantiation_rule):
    '''
    Instantiation rule 018 checks for a single space between map and (
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Ensure a single space exists between "map" and (.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericKeyword or oLine.isInstantiationPortKeyword:
                if not re.match('^.*\smap\s\(', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'map')
