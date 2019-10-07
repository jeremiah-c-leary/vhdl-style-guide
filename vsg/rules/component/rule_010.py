
from vsg.rules import case_rule
from vsg import utils


class rule_010(case_rule):
    '''
    Component rule 010 checks the "end" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'component', '010', 'isComponentEnd')
        self.solution = 'Change end keyword to ' + self.case + 'case'

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
