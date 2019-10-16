from vsg.rules import prefix_rule
from vsg import utils


class rule_004(prefix_rule):
    '''
    Subtype rule 004 checks for prefixes in user defined subtype identifiers.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'subtype', '004', 'isSubtypeKeyword')
        self.prefixes = ['st_']
        self.solution = 'Subtype'

    def _extract(self, oLine):
        return utils.extract_type_identifier(oLine)
