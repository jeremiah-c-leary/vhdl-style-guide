
from vsg.rules.generate import generate_rule
from vsg import check


class rule_004(generate_rule):
    '''Generate rule 004 checks for a blank line before the "generate" keyword.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Add blank line above the "generate" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword:
                check.is_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
