
from vsg.rules import uppercase_end_label


class rule_019(uppercase_end_label):
    '''
    Process rule 019 checks the "end process" label is uppercase.
    '''

    def __init__(self):
        uppercase_end_label.__init__(self, 'process', '019', 'isEndProcess')
