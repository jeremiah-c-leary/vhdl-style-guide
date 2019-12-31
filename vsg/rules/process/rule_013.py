
from vsg.rules import case_rule
from vsg import utils


class rule_013(case_rule):
    '''
    Process rule 013 checks the "is" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'process', '013', 'isSensitivityListEnd')
        self.solution = 'Change "is" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['is'])
