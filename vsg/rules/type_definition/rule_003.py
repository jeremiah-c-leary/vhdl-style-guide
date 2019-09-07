
from vsg.rules import multiple_spaces_after_rule


class rule_003(multiple_spaces_after_rule):
    '''
    Type rule 003 checks the spaces after the "type" keyword.
    '''

    def __init__(self):
        multiple_spaces_after_rule.__init__(self, 'type', '003', 'isTypeKeyword', 'type')
