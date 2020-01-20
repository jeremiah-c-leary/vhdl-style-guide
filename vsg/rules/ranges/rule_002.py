
from vsg.rules import case_rule
from vsg import utils


class rule_002(case_rule):
    '''
    Ranges rule 002 checks the "to" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'range', '002')
        self.solution = 'Change "to" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['to'])
