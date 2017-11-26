
from vsg.rules.generate import generate_rule
from vsg import check


class rule_001(generate_rule):
    '''Generate rule 001 checks for spaces at the beginning of the line.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword or oLine.isGenerateBegin or oLine.isGenerateEnd:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
