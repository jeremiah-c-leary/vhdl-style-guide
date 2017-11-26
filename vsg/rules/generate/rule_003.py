
from vsg.rules.generate import generate_rule
from vsg import check


class rule_003(generate_rule):
    '''Generate rule 003 checks for a blank line after the "end generate" keywords.'''

    def __init__(self):
        generate_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line below the "end generate" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateEnd:
                check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)
