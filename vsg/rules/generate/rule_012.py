
from vsg.rules import case_rule
from vsg import utils


class rule_012(case_rule):
    '''
    Generate rule 012 checks the "end generate" label has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'generate', '012', 'isGenerateEnd')
        self.case = 'upper'
        self.solution = 'Change end generate label to '

    def _extract(self, oLine):
        return utils.extract_end_label(oLine)
