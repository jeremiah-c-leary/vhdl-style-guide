
from vsg.rules.component import component_rule

import re


class rule_007(component_rule):
    '''Component rule 007 checks for a single space before the "is" keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove extra spaces before "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                if len(oLine.line.split()) > 2:
                    self._is_single_space_before('is', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'\s+(is)', r' \1', oLine.line, flags=re.IGNORECASE))
