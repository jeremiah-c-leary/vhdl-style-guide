
from vsg.rules import remove_spaces_before_character_rule


class rule_004(remove_spaces_before_character_rule):
    '''
    Whitespace rule 004 checks for spaces before commas.
    '''

    def __init__(self):
        remove_spaces_before_character_rule.__init__(self, 'whitespace', '004', ',')
        self.solution = 'Remove spaces before commas.'
