
from vsg.rules import single_space_before_character_rule


class rule_024(single_space_before_character_rule):
    '''
    Process rule 024 checks for a single space after the process label and the :.
    '''

    def __init__(self):
        single_space_before_character_rule.__init__(self, 'process', '024', 'isProcessLabel', ':')
        self.solution = 'Ensure a single space exists between process label and :.'
