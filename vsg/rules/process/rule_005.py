
from vsg.rules import case_rule
from vsg import utils


class rule_005(case_rule):
    '''
    Process rule 004 checks the "process" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'process', '005', 'isProcessKeyword')
        self.solution = 'Change "process" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['process'])
