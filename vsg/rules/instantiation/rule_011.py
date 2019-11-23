
from vsg.rules import case_rule
from vsg import utils


class rule_011(case_rule):
    '''
    Instantiation rule 011 checks the port name has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '011', 'isInstantiationPortAssignment')
        self.case = 'upper'
        self.solution = 'Change port name to '

    def _extract(self, oLine):
        return utils.extract_port_names_from_port_map(oLine)
