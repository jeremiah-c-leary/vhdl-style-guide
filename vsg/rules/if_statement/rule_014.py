
from vsg.rules import indent_rule


class rule_014(indent_rule):
    '''
    If rule 014 checks the indent of the "end if" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'if', '014', 'isEndIfKeyword')
