
from vsg import rule
from vsg import utils

import re


class rule_024(rule.rule):
    '''
    Architecture rule 024 checks for the architecture name in the "end architecture" statement.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '024')
        self.solution = 'Add architecture name keyword.'
        self.phase = 1

    def _pre_analyze(self):
        self.sLabel = ""

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isArchitectureKeyword:
            self.sLabel = oLine.line.split()[1]
        if oLine.isEndArchitecture and not re.match('^\s*end\s+architecture\s+\w+', oLine.line, re.IGNORECASE):
            if re.match('^\s*end\s+architecture', oLine.line, re.IGNORECASE):
                dViolation = utils.create_violation_dict(iLineNumber)
                dViolation['label'] = self.sLabel
                self.add_violation(dViolation)
            elif not re.match('^\s*end\s+\w+', oLine.line, re.IGNORECASE):
                dViolation = utils.create_violation_dict(iLineNumber)
                dViolation['label'] = self.sLabel
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            sLine = oLine.line
            sLabel = dViolation['label'] 
            oLine.update_line(sLine.replace(';', ' ' + sLabel.upper() + ';', 1))
