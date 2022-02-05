
from vsg.rules import file_length


class rule_002(file_length):
    '''
    This rule checks the length of a file.

    Refer to `Configuring Length Rules <configuring_length_rules.html>`_ for configuring this option.
    '''

    def __init__(self):
        file_length.__init__(self, 'length', '002')
