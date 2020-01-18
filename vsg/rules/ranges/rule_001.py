
from vsg.rules import case_rule
from vsg import utils


class rule_001(case_rule):
    '''
    Ranges rule 001 checks the "downto" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'range', '001')
        self.solution = 'Change "downto" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['downto'])
