
from vsg.rules import indent_rule


class rule_012(indent_rule):
    '''
    If rule 012 checks the indent of the "if" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'if', '012', 'isElseIfKeyword')
