
from vsg.rules import case_rule
from vsg import utils


class rule_009(case_rule):
    '''
    Process rule 009 checks the "end" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'generate', '009', 'isGenerateEnd')
        self.solution = 'Change "end" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
