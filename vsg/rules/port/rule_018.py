
from vsg.rules import case_rule
from vsg import utils


class rule_018(case_rule):
    '''
    Port rule 018 checks the port type has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'port', '018', 'isPortDeclaration')
        self.solution = 'Change port type name to '

    def _extract(self, oLine):
        return utils.extract_type_name_from_port_vhdl_only(oLine)
