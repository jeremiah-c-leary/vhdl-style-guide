
from vsg.rules import prefix_rule
from vsg import utils


class rule_012(prefix_rule):
    '''
    Variable rule 012 checks for prefixes in variable identifiers.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'variable', '012', 'isVariable')
        self.prefixes = ['v_']
        self.solution = 'Variable'

    def _extract(self, oLine):
        return utils.extract_class_identifier_list(oLine)
