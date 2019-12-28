
from vsg.rules import case_rule
from vsg import utils


class rule_021(case_rule):
    '''
    Entity rule 021 checks the begin keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '021', 'isArchitectureBegin')
        self.solution = 'Change "begin" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['begin'])
