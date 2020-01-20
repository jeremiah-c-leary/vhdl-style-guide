
from vsg.rules import case_rule
from vsg import utils


class rule_013(case_rule):
    '''
    Architecture rule 013 checks the architecture name has proper case in the architecture declaration.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '013', 'isArchitectureKeyword')
        self.case = 'upper'
        self.solution = 'Change architecture name to '

    def _extract(self, oLine):
        return utils.extract_architecture_identifier(oLine)
