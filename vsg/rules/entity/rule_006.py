
from vsg.rules import case_rule
from vsg import utils


class rule_006(case_rule):
    '''
    Entity rule 006 checks the is keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'entity', '006', 'isEntityDeclaration')
        self.solution = 'Change "is" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['is'])
