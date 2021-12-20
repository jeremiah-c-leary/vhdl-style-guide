
from vsg import rule
from vsg import violation
from vsg.rule_group import structure


class rule_001(structure.Rule):
    '''
    Checks the length of the file and determines if the file is empty.
    '''

    def __init__(self):
        structure.Rule.__init__(self, 'source_file', '001')
        # These are filled out when creating a new rule
        self.fixable = False
        self.solution = 'File empty.'

    def analyze(self, oFile):
        oToi = oFile.get_all_tokens()
        iStartIndex = oToi.get_start_index()
        iEndIndex = oToi.get_end_index()

        if oFile.eError:
            oViolation = violation.New(0, oToi, oFile.eError.args[1])
            self.add_violation(oViolation)

        elif iStartIndex == iEndIndex:
            oViolation = violation.New(0, oToi, self.solution)
            self.add_violation(oViolation)
