
from vsg.rules import line_length


class rule_001(line_length):
    '''
    This rule checks the length of the line.

    Refer to `Configuring Length Rules <configuring_length_rules.html>`_ for configuring this option.
    '''

    def __init__(self):
        line_length.__init__(self, 'length', '001')
