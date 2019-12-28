
from vsg.rules import case_rule
from vsg import utils


class rule_004(case_rule):
    '''
    Entity rule 004 checks the architecture keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '004', 'isArchitectureKeyword')
        self.solution = 'Change "architecture" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['architecture'])
