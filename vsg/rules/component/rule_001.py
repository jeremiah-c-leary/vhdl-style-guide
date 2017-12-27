
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Component rule 001 checks for spaces before the "component" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'component', '001', 'isComponentDeclaration')
