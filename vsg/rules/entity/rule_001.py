
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Entity rule 001 checks for spaces before the entity keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'entity', '001', 'isEntityDeclaration')
