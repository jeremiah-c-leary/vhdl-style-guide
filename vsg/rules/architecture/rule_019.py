
from vsg.rules import case_rule
from vsg import utils


class rule_019(case_rule):
    '''
    Entity rule 019 checks the of keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '019', 'isArchitectureKeyword')
        self.solution = 'Change "of" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['of'])
