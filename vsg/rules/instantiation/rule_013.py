
from vsg.rules import case_rule
from vsg import utils


class rule_013(case_rule):
    '''
    Instantiation rule 013 checks the "generic map" keywords have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '013', 'isInstantiationGenericKeyword')
        self.solution = 'Change "generic map" keywords to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['generic', 'map'])
