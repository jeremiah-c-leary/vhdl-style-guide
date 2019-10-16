
from vsg.rules import suffix_rule
from vsg import utils


class rule_025(suffix_rule):
    '''
    Port rule 025 checks for suffixes in port names.
    '''

    def __init__(self):
        suffix_rule.__init__(self, 'port', '025', 'isPortDeclaration')
        self.suffixes = ['_I', '_O', '_IO']
        self.solution = 'Port'

    def _extract(self, oLine):
        return utils.extract_port_name(oLine)
