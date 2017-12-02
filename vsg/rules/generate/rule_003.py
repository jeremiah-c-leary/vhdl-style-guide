
from vsg.rules import line_below_rule


class rule_003(line_below_rule):
    '''
    Generate rule 003 checks for a blank line after the "end generate" keywords.
    '''

    def __init__(self):
        line_below_rule.__init__(self)
        self.name = 'generate'
        self.identifier = '003'
        self.condition = 'isGenerateEnd'
