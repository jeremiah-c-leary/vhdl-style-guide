
from vsg.rules import prefix_rule
from vsg import utils


class rule_015(prefix_rule):
    '''
    Type rule 015 checks for prefixes in user defined type identifiers.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'type', '015', 'isTypeKeyword')
        self.prefixes = ['t_']
        self.solution = 'Type'

    def _extract(self, oLine):
        return utils.extract_type_identifier(oLine)
