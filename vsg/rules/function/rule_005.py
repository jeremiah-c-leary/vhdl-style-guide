
from vsg.rules import case_rule
from vsg import utils


class rule_005(case_rule):
    '''
    Function rule 005 checks the function keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'function', '005', 'isFunctionKeyword')
        self.solution = 'Change "function" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['function'])
