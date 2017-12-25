
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Attribute rule 001 checks the indent of attribute statements.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'attribute', '001', 'insideAttribute')
