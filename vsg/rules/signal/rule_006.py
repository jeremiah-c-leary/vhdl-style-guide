
from vsg.rules import single_space_before_character_rule


class rule_006(single_space_before_character_rule):
    '''
    Signal rule 006 checks there is at least a single space before the colon.
    '''

    def __init__(self):
        single_space_before_character_rule.__init__(self, 'signal', '006', 'isSignal', ':')
        self.solution = 'Add a single space before the colon.'
