
from vsg.rules import multiple_spaces_after_rule


class rule_003(multiple_spaces_after_rule):
    '''
    File rule 003 checks for a single space after the **attribute** keyword.
    '''

    def __init__(self):
        multiple_spaces_after_rule.__init__(self, 'file', '003', 'isFileKeyword', 'file')
        self.solution = 'Ensure a single space after the "file" keyword.'
