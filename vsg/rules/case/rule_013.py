
from vsg.rules import indent_rule


class rule_013(indent_rule):
    '''
    Case rule 013 verifies the indent of the "Null" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'case', '013', 'isCaseNull')
