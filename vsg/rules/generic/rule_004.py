
from vsg.rules import indent_rule


class rule_004(indent_rule):
    '''
    Generic rule 004 checks indentation of generics.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'generic', '004', 'isGenericDeclaration', 'isEndGenericMap')
