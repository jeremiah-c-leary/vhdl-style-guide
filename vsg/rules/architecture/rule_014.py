
from vsg.rules.architecture import architecture_rule

import re


class rule_014(architecture_rule):
    '''Architecture rule 013 checks the entity name is upper case in the architecture declaration.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Upper case entity name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                if re.match('^\s*\S+\s\s*\S+\s\s*of\s\s*\S+\s\s*is', oLine.lineLower):
                    lLine = oLine.line.split()
                    self._is_uppercase(lLine[3], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[3])
