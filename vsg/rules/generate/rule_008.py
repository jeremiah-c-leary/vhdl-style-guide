
from vsg.rules import single_space_after_rule


class rule_008(single_space_after_rule):
    '''
    Process rule 007 checks for a single space between the "end" and "generate" keywords.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'generate', '008', 'isGenerateEnd', 'end')
        self.solution = 'Ensure there is only one space between the "end" and "generate" keywords.'
