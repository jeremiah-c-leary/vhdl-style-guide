
from vsg.rules.variable_assignment import variable_assignment_rule

import re


class rule_002(variable_assignment_rule):
    '''Variable assignment rule 002 checks for a single space after the ":=" keyword.'''

    def __init__(self):
        variable_assignment_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists after the ":=" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment:
                if re.match('^.*:=\s*\S', oLine.line):
                    if not re.match('^.*:=\s\S', oLine.line):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':=')
