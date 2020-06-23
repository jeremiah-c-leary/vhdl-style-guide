
from vsg.rules import case_rule
from vsg import utils


class rule_018(case_rule):
    '''
    Package rule 018 checks the "package" keyword in the "end package" has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'package', '018', 'isPackageEnd')
        self.solution = 'Change "package" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['package'])
