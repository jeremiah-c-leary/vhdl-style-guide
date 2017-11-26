
from vsg.rules.architecture import architecture_rule


class rule_005(architecture_rule):
    '''Architecture rule 005 checks if the "of" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure "of" keyword is on the same line as the "architecture" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                lLine = oLine.lineLower.split()
                if len(lLine) < 3:
                    self.add_violation(iLineNumber)
                elif not lLine[2] == "of":
                    self.add_violation(iLineNumber)
