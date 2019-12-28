
from vsg.rules import case_rule
from vsg import utils


class rule_014(case_rule):
    '''
    Entity rule 014 checks the entity keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'entity', '014', 'isEndEntityDeclaration')
        self.solution = 'Change "entity" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['entity'])
