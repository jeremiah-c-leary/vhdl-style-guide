
from vsg.rules import case_rule
from vsg import utils


class rule_017(case_rule):
    '''
    Port rule 017 checks the "port" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'port', '017', 'isPortKeyword')
        self.solution = 'Change "port" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)