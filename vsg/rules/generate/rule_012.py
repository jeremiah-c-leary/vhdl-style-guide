
from vsg.rules import uppercase_end_label


class rule_012(uppercase_end_label):
    '''
    Generate rule 012 checks the "end generate" label is uppercase.
    '''

    def __init__(self):
        uppercase_end_label.__init__(self, 'generate', '012', 'isGenerateEnd')
