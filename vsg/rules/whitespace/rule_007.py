
from vsg import rule

import re


class rule_007(rule.rule):
    '''Whitespace rule 007 checks for spaces after a comma.'''

    def __init__(self):
        rule.rule.__init__(self, 'whitespace', '007')
        self.phase = 2
        self.solution = 'Add a space after the comma.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if re.match('^.*,\S', oLine.line) and not re.match('^.*--.*,\S', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r',(\S)', r', \1', oLine.line))
