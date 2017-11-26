
from vsg.rules.generate import generate_rule


class rule_005(generate_rule):
    '''Generate rule 005 checks the generate label is uppercase.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Uppercase generate label.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                lLine = oLine.line.split(':')
                if not lLine[0] == lLine[0].upper():
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split(':')[0].lstrip().rstrip())
