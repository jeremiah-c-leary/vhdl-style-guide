
from vsg.rules.component import component_rule

import re


class rule_002(component_rule):
    '''
    Component rule 002 checks for a single space after the "component" keyword.
    '''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces after "component" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                if re.match('^\s*component\s\s+\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'component')
