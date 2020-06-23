
from vsg.rules import case_rule
from vsg import utils


class rule_008(case_rule):
    '''
    Procedure rule 008 checks the "end" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'procedure', '008', 'isProcedureEnd')
        self.solution = 'Change "end" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['end'])
