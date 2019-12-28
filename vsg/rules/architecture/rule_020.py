
from vsg.rules import case_rule
from vsg import utils


class rule_020(case_rule):
    '''
    Entity rule 020 checks the is keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '020', 'isArchitectureKeyword')
        self.solution = 'Change "is" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['is'])
