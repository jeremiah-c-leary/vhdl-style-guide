
from vsg import rule

import re


class rule_028(rule.rule):
    '''
    Instantiation rule 028 checks the entity name is uppercase in direct instantiations.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '028'
        self.solution = 'Uppercase entity name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isDirectInstantiationDeclaration and not re.match('^\s*\w+\s*:\s*\w+\s+\w+\.[A-Z0-9_]+', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            sWord = oLine.line.split('.')[1].split()[0].upper()
            oLine.update_line(re.sub('\.(\w+)', '.' + sWord, oLine.line, 1, re.IGNORECASE))
