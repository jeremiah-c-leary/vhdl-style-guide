
from vsg.rules.whitespace import whitespace_rule

import re


class rule_007(whitespace_rule):
    '''Whitespace rule 007 checks for spaces after a comma.'''

    def __init__(self):
        whitespace_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Add a space after the comma.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if re.match('^.*,\S', oLine.line) and not re.match('^.*--.*,\S', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r',(\S)', r', \1', oLine.line))
