
from vsg.rules import case_rule
from vsg import utils


class rule_010(case_rule):
    '''
    Signal rule 010 checks the signal type has proper case if it is a VHDL keyword.
    '''

    def __init__(self):
        case_rule.__init__(self, 'signal', '010', 'isSignal')
        self.solution = 'Change signal type name to '
        self.disabled = True

    def _extract(self, oLine):
        return utils.extract_type_name_vhdl_only(oLine)
