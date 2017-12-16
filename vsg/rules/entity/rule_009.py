
from vsg.rules import indent_rule


class rule_009(indent_rule):
    '''
    Entity rule 009 checks for spaces before the "end" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'entity', '009', 'isEndEntityDeclaration')
