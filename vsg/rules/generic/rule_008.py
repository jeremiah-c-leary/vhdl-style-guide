
from vsg.rules import indent_rule


class rule_008(indent_rule):
    '''
    Generic rule 008 checks the indentation of closing parenthesis for generic maps.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'generic', '008', 'isEndGenericMap', 'isGenericDeclaration')
