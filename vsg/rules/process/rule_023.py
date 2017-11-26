
from vsg.rules.process import process_rule
from vsg import check


class rule_023(process_rule):
    '''
    Process rule 023 checks for a blank line above the "end process" keywords.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '023'
        self.solution = 'Add blank line above the "end process" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                check.is_blank_line_before(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_above(oFile, iLineNumber)
