
from vsg.rules import case_rule
from vsg import utils


class rule_004(case_rule):
    '''
    Function rule 004 checks the "begin" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'function', '004', 'isFunctionBegin')
        self.solution = 'Change "begin" keyword to '

    def _extract(self, oLine):
        return utils.extract_word(oLine, 'begin')
