
from vsg.rules import single_space_after_rule


class rule_004(single_space_after_rule):
    '''
    Case rule 004 checks for a single space after the "when" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'case', '004', 'isCaseWhenKeyword', 'when')
        self.solution = 'Ensure a single space exists after the "when" keyword.'
