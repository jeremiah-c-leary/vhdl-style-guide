
from vsg.rules import prefix_rule
from vsg import utils


class rule_008(prefix_rule):
    '''
    Signal rule 008 checks for prefixes in signal identifiers.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'signal', '008', 'isSignal')
        self.prefixes = ['s_']
        self.solution = 'Signal'

    def _extract(self, oLine):
        return utils.extract_class_identifier_list(oLine)
