
from vsg.rules import case_rule
from vsg import utils


class rule_005(case_rule):
    '''
    Generate rule 005 checks the label has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'generate', '005', 'isGenerateLabel')
        self.solution = 'Change label to ' + self.case + 'case'
        self.case = 'upper'

    def _extract(self, oLine):
        return utils.extract_label(oLine)
