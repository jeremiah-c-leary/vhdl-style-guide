
from vsg.rules import case_rule
from vsg import utils


class rule_005(case_rule):
    '''
    Library rule 005 checks the use keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'library', '005', 'isLibraryUse')
        self.solution = 'Change "use" keyword to '

    def _extract(self, oLine):
        return utils.extract_first_keyword(oLine)
