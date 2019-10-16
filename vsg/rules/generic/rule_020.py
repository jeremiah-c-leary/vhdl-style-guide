
from vsg.rules import prefix_rule
from vsg import utils


class rule_020(prefix_rule):
    '''
    Generic rule 020 checks for prefixes in generic names.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'generic', '020', 'isGenericDeclaration')
        self.prefixes = ['G_']
        self.solution = 'Generic'

    def _extract(self, oLine):
        return utils.extract_generics(oLine)
