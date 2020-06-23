
from vsg.rules import case_rule
from vsg import utils


class rule_009(case_rule):
    '''
    Procedure rule 009 checks the "procedure" keyword in the "end procedure" has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'procedure', '009', 'isProcedureEnd')
        self.solution = 'Change "procedure" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['procedure'])
