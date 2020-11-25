
from vsg.rules import line_length


class rule_001(line_length):
    '''
    Checks for line length violations.
    '''

    def __init__(self):
        line_length.__init__(self, 'length', '001')
