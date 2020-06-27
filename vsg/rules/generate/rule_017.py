
from vsg.rules import prefix_rule
from vsg import utils


class rule_017(prefix_rule):
    '''
    Generate rule 017 checks for prefixes in generate statement labels.
    '''

    def __init__(self):
        prefix_rule.__init__(self, 'generate', '017', 'isGenerateLabel')
        self.prefixes = ['gen_']
        self.solution = 'Generate label'

    def _extract(self, oLine):
        return utils.extract_label(oLine)
