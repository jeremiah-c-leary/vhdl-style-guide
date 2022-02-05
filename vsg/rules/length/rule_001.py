
from vsg.rules import line_length


class rule_001(line_length):
    '''
    This rule checks the length of the line.

    |configuring_length_rules_link|
    '''

    def __init__(self):
        line_length.__init__(self, 'length', '001')
