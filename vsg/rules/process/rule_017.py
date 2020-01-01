
from vsg.rules import case_rule
from vsg import utils


class rule_017(case_rule):
    '''
    Process rule 017 checks the process label has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'process', '017', 'isProcessLabel')
        self.case = 'upper'
        self.solution = 'Change label name to '

    def _extract(self, oLine):
        return utils.extract_label(oLine)
