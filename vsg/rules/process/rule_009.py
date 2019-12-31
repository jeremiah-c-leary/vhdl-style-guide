
from vsg.rules import case_rule
from vsg import utils


class rule_009(case_rule):
    '''
    Process rule 009 checks the "process" keyword has proper case on the closing of a process.
    '''

    def __init__(self):
        case_rule.__init__(self, 'process', '009', 'isEndProcess')
        self.solution = 'Change "process" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['process'])
