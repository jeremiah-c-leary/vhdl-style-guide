
from vsg import rule

import re


class rule_027(rule.rule):
    '''
    Instantiation rule 027 checks the **entity** keyword is lowercase in direct instantiations.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '027'
        self.solution = 'Uppercase "entity" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isDirectInstantiationDeclaration and not re.match('^\s*\w+\s*:\s*entity', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('entity', 'entity', oLine.line, 1, re.IGNORECASE))
