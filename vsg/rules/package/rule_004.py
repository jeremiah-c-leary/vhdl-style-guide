
from vsg.rules import case_rule
from vsg import utils


class rule_004(case_rule):
    '''
    Package rule 004 checks the "package" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'package', '004', 'isPackageKeyword')
        self.solution = 'Change "package" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
