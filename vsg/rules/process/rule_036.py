from vsg.rules import prefix_rule
from vsg import utils


class rule_036(prefix_rule):
    '''
    Process rule 036 checks for prefixes in process labels.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'process', '036', 'isProcessLabel')
        self.prefixes = ['proc_']
        self.solution = 'Process labels'

    def _extract(self, oLine):
        return utils.extract_label(oLine)
