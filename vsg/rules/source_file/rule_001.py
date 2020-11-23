
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils


class rule_001(rule.Rule):
    '''
    Checks the length of the file and determines if the file is empty.
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'source_file', '001')
        self.phase = 1
        # These are filled out when creating a new rule
        self.fixable = False
        self.solution = 'File not found.'

    def analyze(self, oFile):
        oToi = oFile.get_all_tokens()
        iStartIndex = oToi.get_start_index()
        iEndIndex = oToi.get_end_index()
        if iStartIndex == iEndIndex:
            oViolation = violation.New(0, oToi, self.solution)
            self.add_violation(oViolation)
