
from vsg.rules import case_rule
from vsg import utils


class rule_018(case_rule):
    '''
    Entity rule 018 checks the case keyword has proper case in end case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'case', '018', 'isEndCaseKeyword')
        self.solution = 'Change "case" keyword to '

    def _extract(self, oLine):
        return utils.extract_word(oLine, 'case')
