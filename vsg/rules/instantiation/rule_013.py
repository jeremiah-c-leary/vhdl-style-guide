
from vsg.rules.instantiation import instantiation_rule

import re


class rule_013(instantiation_rule):
    '''
    Instantiation rule 013 checks the "generic map" keywords are lower case.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Change "generic map" keywords to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericKeyword:
                if not re.match('^.*generic\s+map', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'generic')
            self._lower_case(oFile.lines[iLineNumber], 'map')
