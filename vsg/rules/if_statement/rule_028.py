
from vsg.rules import case_rule
from vsg import utils


class rule_028(case_rule):
    '''
    If rule 028 checks the **end if** keywords have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'if', '028', 'isEndIfKeyword')
        self.solution = 'Change "end if" keywords to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['end', 'if'])
