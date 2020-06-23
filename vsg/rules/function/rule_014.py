
from vsg.rules import case_rule
from vsg import utils


class rule_014(case_rule):
    '''
    Function rule 014 checks the "function" keyword in the "end function" has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'function', '014', 'isFunctionEnd')
        self.solution = 'Change "function" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['function'])
