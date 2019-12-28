
from vsg.rules import case_rule
from vsg import utils


class rule_006(case_rule):
    '''
    Component rule 006 checks the is keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'component', '006', 'isComponentDeclaration')
        self.solution = 'Change "is" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['is'])
