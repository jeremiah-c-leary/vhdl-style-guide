
from vsg.rules.architecture import architecture_rule


class rule_006(architecture_rule):
    '''Architecture rule 006 checks if the "is" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure "is" keyword is on the same line as the "architecture" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                lLine = oLine.lineLower.split()
                if len(lLine) < 5:
                    self.add_violation(iLineNumber)
                elif not lLine[4] == "is":
                    self.add_violation(iLineNumber)
