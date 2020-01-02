
from vsg.rules import case_rule
from vsg import utils


class rule_006(case_rule):
    '''
    Instantiation rule 006 checks the "port map" keywords have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '006', 'isInstantiationPortKeyword')
        self.solution = 'Change "port map" keywords to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['port', 'map'])
