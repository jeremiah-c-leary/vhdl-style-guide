
from vsg import rule
from vsg import fix
from vsg import check


class rule_011(rule.rule):
    '''
    Architecture rule 011 checks the architecture name is upper case on the closing "end architecture" line.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '011')
        self.solution = 'Uppercase architecture name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if not lLine[2].startswith('--'):
                        check.is_uppercase(self, lLine[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[2])
