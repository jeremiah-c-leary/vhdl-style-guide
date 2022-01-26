
from vsg.rules import file_length


class rule_002(file_length):
    '''
    This rule checks the length of a file.

    Refer to the section `Configuring Length Rules <configuring.html#configuring-length-rules>`_ for configuring this option.
    '''

    def __init__(self):
        file_length.__init__(self, 'length', '002')
