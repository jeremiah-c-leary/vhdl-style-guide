
from vsg.rules import case_rule
from vsg import utils


class rule_013(case_rule):
    '''
    Entity rule 013 checks the "is" keyword has proper case in type definitions.
    '''

    def __init__(self):
        case_rule.__init__(self, 'type', '013', 'isTypeKeyword')
        self.solution = 'Change "is" keyword to '

    def _extract(self, oLine):
        return utils.extract_word(oLine, 'is')
