
from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    File rule 003 checks for a single space after the **attribute** keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'file', '003', 'isFileKeyword', 'file')
        self.solution = 'Ensure a single space after the "file" keyword.'
