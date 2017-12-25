
from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    Attribute rule 003 checks for a single space after the **attribute** keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'attribute', '003', 'isAttributeKeyword', 'attribute')
        self.solution = 'Ensure a single space after the "attribute" keyword.'
