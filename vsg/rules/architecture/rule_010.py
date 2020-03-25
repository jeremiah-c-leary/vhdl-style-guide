
from vsg import rule
from vsg import utils

import re


class rule_010(rule.rule):
    '''
    Architecture rule 010 checks for "architecture" in the "end architecture statement.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'architecture'
        self.identifier = '010'
        self.solution = 'Add "architecture" keyword after "end" keyword.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isEndArchitecture:
            if not re.match('^\s*end\s+architecture', oLine.line, re.IGNORECASE):
                self.add_violation(utils.create_violation_dict(iLineNumber))

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub(r'^(\s*end)', r'\1 architecture', oLine.line, flags=re.IGNORECASE))
