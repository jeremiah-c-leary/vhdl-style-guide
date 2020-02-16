
from vsg.rules import single_space_before_character_rule

class rule_004(single_space_before_character_rule):
    '''
    Concurrent rule 004 checks there is at least a single space before the assignment.
    '''

    def __init__(self):
        single_space_before_character_rule.__init__(self, 'concurrent', '004', 'isConcurrentBegin', '<=')
        self.solution = 'Add a single space before the <=.'
