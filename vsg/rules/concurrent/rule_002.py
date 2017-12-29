
from vsg.rules import single_space_after_character_rule


class rule_002(single_space_after_character_rule):
    '''
    Concurrent rule 002 checks there is a single space after the assignment.
    '''

    def __init__(self):
        single_space_after_character_rule.__init__(self, 'concurrent', '002', 'isConcurrentBegin', '<=')
        self.solution = 'Remove all but one space after the <=.'
