
from vsg import rule
from vsg import fix
from vsg import utils

import re


class rule_032(rule.rule):
    '''
    Instantiation rule 032 checks for a single space after the component keyword if used.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '032'
        self.solution = 'Lowercase the component keyword'
        self.phase = 2
        self.disable = True

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationDeclaration and not oLine.isDirectInstantiationDeclaration:
            if re.match('^\s*\w+\s*:\s*component', oLine.line, flags=re.IGNORECASE):
                if not re.match('^\s*\w+\s*:\s*component\s\w', oLine.line, flags=re.IGNORECASE):
                    dViolation = utils.create_violation_dict(iLineNumber)
                    self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            fix.enforce_one_space_after_word(self, utils.get_violating_line(oFile, dViolation), 'component')
