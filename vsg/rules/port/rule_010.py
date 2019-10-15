
from vsg.rules import case_rule
from vsg import utils


class rule_010(case_rule):
    '''
    Port rule 010 checks port names have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'port', '010', 'isPortDeclaration')
        self.case = 'upper'
        self.solution = 'Change port name to '

    def _extract(self, oLine):
        return utils.extract_port_name(oLine)
