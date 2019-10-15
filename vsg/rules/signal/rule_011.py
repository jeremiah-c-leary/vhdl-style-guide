
from vsg.rules import case_rule
from vsg import utils


class rule_011(case_rule):
    '''
    Signal rule 011 checks the signal type has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'signal', '011', 'isSignal')
        self.solution = 'Change signal type name to '

    def _extract(self, oLine):
        return utils.extract_type_name(oLine)
