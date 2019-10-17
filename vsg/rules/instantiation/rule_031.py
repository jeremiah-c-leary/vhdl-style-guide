
from vsg import rule
from vsg import fix

import re


class rule_031(rule.rule):
    '''
    Instantiation rule 031 checks the component keyword is lowercase if it is used.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '031'
        self.solution = 'Lowercase the component keyword'
        self.phase = 6
        self.disable = True

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationDeclaration and not oLine.isDirectInstantiationDeclaration:
            if re.match('^\s*\w+\s*:\s*component', oLine.line, flags=re.IGNORECASE):
                if not re.match('^\s*\w+\s*:\s*component', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(oFile.lines[iLineNumber], 'component')
