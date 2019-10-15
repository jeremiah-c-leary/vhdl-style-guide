
from vsg.rules import case_rule
from vsg import utils


class rule_019(case_rule):
    '''
    Process rule 019 checks the "end process" label has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'process', '019', 'isEndProcess')
        self.case = 'upper'
        self.solution = 'Change end process label to '

    def _extract(self, oLine):
        return utils.extract_end_label(oLine)
