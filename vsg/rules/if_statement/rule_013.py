
from vsg.rules import indent_rule


class rule_013(indent_rule):
    '''
    If rule 013 checks the indent of the "else" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'if', '013', 'isElseKeyword')
