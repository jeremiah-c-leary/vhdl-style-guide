
from vsg.rules import remove_spaces_before_character_rule


class rule_003(remove_spaces_before_character_rule):
    '''
    Whitespace rule 003 checks for spaces before semicolons
    '''

    def __init__(self):
        remove_spaces_before_character_rule.__init__(self, 'whitespace', '003', ';')
        self.solution = 'Remove spaces before semicolons.'
