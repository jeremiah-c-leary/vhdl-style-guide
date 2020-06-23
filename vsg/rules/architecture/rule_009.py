
from vsg.rules import case_rule
from vsg import utils


class rule_009(case_rule):
    '''
    Architecture rule 009 checks the "end" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '009', 'isEndArchitecture')
        self.solution = 'Change "end" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['end'])
