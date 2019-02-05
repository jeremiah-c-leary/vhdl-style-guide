
from vsg.rules import single_space_after_rule


class rule_013(single_space_after_rule):
    '''
    Generate rule 013 checks for a single space between "generate" keyword and the label.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'generate', '013', 'isGenerateEnd', 'generate')
        self.solution = 'Ensure there is only one space between the "generate" keyword and the label.'
