
from vsg.rules import indent_rule


class rule_012(indent_rule):
    '''
    Type rule 012 checks the indent of record elements.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'type', '012', 'insideTypeRecord')
