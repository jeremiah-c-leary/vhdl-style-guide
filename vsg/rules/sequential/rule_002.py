
from vsg.rules import single_space_after_character_rule


class rule_002(single_space_after_character_rule):
    '''
    Sequential rule 002 checks for a single space after the "<=" keyword.
    '''

    def __init__(self):
        single_space_after_character_rule.__init__(self, 'sequential', '002', 'isSequential', '<=')
        self.solution = 'Ensure a single space exists after the "<=" keyword.'
