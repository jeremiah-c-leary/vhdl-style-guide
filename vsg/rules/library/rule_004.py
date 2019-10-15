
from vsg.rules import case_rule
from vsg import utils


class rule_004(case_rule):
    '''
    Library rule 004 checks the library keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'library', '004', 'isLibrary')
        self.solution = 'Change "library" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
