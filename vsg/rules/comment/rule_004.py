
from vsg.rules import single_space_before_character_rule


class rule_004(single_space_before_character_rule):
    '''
    Comment rule 004 ensures there is at least one space before comments on a line with code.
    '''

    def __init__(self):
        single_space_before_character_rule.__init__(self, 'comment', '004', 'hasInlineComment', '--')
        self.solution = 'Add a space before the comment --'
