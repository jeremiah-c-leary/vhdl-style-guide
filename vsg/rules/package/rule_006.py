
from vsg.rules import case_rule
from vsg import utils


class rule_006(case_rule):
    '''
    Package rule 006 checks the "end" and "package" keywords have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'package', '006', 'isPackageEnd')
        self.solution = 'Change "end" and "package" keywords to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['end', 'package'])
