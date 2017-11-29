
from vsg.rules.type import type_rule
from vsg import fix
from vsg import check


class rule_004(type_rule):
    '''
    Type rule 004 checks the type name is lowercase.
    '''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change type name to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                check.is_lowercase(self, oLine.line.split()[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])
