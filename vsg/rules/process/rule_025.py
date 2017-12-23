
from vsg.rules import single_space_after_character_rule


class rule_025(single_space_after_character_rule):
    '''
    Process rule 025 checks for a single space after the : and before the "process" keyword.
    '''

    def __init__(self):
        single_space_after_character_rule.__init__(self, 'process', '025', 'isProcessLabel', ':')
        self.solution = 'Ensure a single space exists between the : and the "process" keyword.'
