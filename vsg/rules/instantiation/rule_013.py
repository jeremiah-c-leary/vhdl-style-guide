
from vsg import rule
from vsg import fix

import re


class rule_013(rule.rule):
    '''
    Instantiation rule 013 checks the "generic map" keywords are lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
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
            fix.lower_case(self, oFile.lines[iLineNumber], 'generic')
            fix.lower_case(self, oFile.lines[iLineNumber], 'map')
