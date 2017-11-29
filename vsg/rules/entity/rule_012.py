
from vsg.rules.entity import entity_rule
from vsg import fix
from vsg import check


class rule_012(entity_rule):
    '''
    Entity rule 012 checks entity name is uppercase in "end" keyword line.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Uppercase entity name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndEntityDeclaration:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    check.is_uppercase(self, lLine[2], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.upper_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[2])
