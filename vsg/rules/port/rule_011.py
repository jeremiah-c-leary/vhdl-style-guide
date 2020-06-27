
from vsg.rules import prefix_rule
from vsg import utils


class rule_011(prefix_rule):
    '''
    Port rule 011 checks for prefixes in port names.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'port', '011', 'isPortDeclaration')
        self.prefixes = ['i_', 'o_', 'io_']
        self.solution = 'Port names'

    def _extract(self, oLine):
        return utils.extract_port_name(oLine)
