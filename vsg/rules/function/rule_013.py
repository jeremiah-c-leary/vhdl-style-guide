
from vsg.rules import case_rule
from vsg import utils


class rule_013(case_rule):
    '''
    Function rule 013 checks the "end" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'function', '013', 'isFunctionEnd')
        self.solution = 'Change "end" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['end'])
