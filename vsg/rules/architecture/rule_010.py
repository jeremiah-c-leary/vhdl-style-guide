
from vsg.rules.architecture import architecture_rule

import re


class rule_010(architecture_rule):
    '''Architecture rule 010 checks for the entity name exists on the same line as the "end" and "architecture" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'End of architecture follows this format: end architecture <architecture name>.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if lLine[2].startswith('--'):
                        self.add_violation(iLineNumber)
                else:
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*end)', r'\1 architecture', oLine.line, flags=re.IGNORECASE))
