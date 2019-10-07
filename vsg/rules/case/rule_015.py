
from vsg.rules import case_rule
from vsg import utils


class rule_015(case_rule):
    '''
    Entity rule 015 checks the is keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'case', '015', 'isCaseIsKeyword', self._extract_is_keyword)
        self.solution = 'Change is keyword to ' + self.case + 'case'

    def _extract_is_keyword(self, oLine):
        return utils.extract_word(oLine.line, 'is')
