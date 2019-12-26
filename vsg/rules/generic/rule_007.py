
from vsg.rules import case_rule
from vsg import utils


class rule_007(case_rule):
    '''
    Generic rule 007 checks generic names have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'generic', '007', 'isGenericDeclaration')
        self.case = 'upper'
        self.solution = 'Change generic name to '

    def _extract(self, oLine):
        return utils.extract_generics(oLine)
