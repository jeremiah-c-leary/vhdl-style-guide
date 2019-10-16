
from vsg.rules import prefix_rule
from vsg import utils


class rule_015(prefix_rule):
    '''
    Constant rule 015 checks for prefixes in constant identifiers.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'constant', '015', 'isConstant')
        self.prefixes = ['c_']
        self.solution = 'Constant'

    def _extract(self, oLine):
        return utils.extract_class_identifier_list(oLine)
