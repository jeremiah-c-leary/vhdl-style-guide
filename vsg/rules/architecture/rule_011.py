
from vsg.rules.architecture import architecture_rule


class rule_011(architecture_rule):
    '''Architecture rule 011 checks the entity name is upper case on the closing "end architecture" line.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Uppercase architecture name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if not lLine[2].startswith('--'):
                        self._is_uppercase(lLine[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[2])
