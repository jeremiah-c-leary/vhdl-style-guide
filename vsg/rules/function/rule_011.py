
from vsg.rules import indent_rule


class rule_011(indent_rule):
    '''
    Function rule 011 checks the indent of function parameters when they are on multiple lines.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'function', '011', 'isFunctionParameterEnd', 'isFunctionParameter')
