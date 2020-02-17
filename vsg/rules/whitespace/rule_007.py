
from vsg import rule
from vsg import utils

import re


class rule_007(rule.rule):
    '''Whitespace rule 007 checks for spaces after a comma.'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '007')
        self.phase = 2
        self.solution = 'Add a space after the comma.'

    def _analyze(self, oFile, oLine, iLineNumber):
        if re.match('^.*,\S', oLine.line) and not re.match('^.*--.*,\S', oLine.line):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub(r',(\S)', r', \1', oLine.line))
