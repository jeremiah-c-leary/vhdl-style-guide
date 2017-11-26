
from vsg.rules.process import process_rule
from vsg import check


class rule_011(process_rule):
    '''
    Process rule 010 checks for a blank line after the "end process" keywords.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Add a blank line after the "end process" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._insert_blank_line_below(oFile, iLineNumber)
