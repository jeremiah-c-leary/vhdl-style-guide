
from vsg.rules import single_space_after_character_rule


class rule_002(single_space_after_character_rule):
    '''
    Variable assignment rule 002 checks for a single space after the ":=" keyword.
    '''

    def __init__(self):
        single_space_after_character_rule.__init__(self, 'variable_assignment', '002', 'isVariableAssignment', ':=')
        self.solution = 'Ensure a single space exists after the ":=" keyword.'
