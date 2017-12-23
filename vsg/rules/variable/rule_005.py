
from vsg.rules import single_space_after_character_rule


class rule_005(single_space_after_character_rule):
    '''
    Signal rule 005 checks there is a single space after the colon.
    '''

    def __init__(self):
        single_space_after_character_rule.__init__(self, 'variable', '005', 'isVariable', ':')
        self.solution = 'Ensure only a variable space after the colon.'
