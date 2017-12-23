
from vsg.rules import single_space_before_character_rule


class rule_003(single_space_before_character_rule):
    '''
    Sequential rule 003 checks for a single space before the "<=" keyword.
    '''

    def __init__(self):
        single_space_before_character_rule.__init__(self, 'sequential', '003', 'isSequential', '<=')
        self.solution = 'Ensure a single space exists before the "<=" keyword.'
