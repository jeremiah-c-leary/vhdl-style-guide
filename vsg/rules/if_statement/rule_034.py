
from vsg.rules import case_rule
from vsg import utils


class rule_034(case_rule):
    '''
    If rule 034 checks the "if" keyword in the "end if" has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'if', '034', 'isEndIfKeyword')
        self.solution = 'Change "if" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['if'])
