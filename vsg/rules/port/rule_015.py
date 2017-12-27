
from vsg.rules import indent_rule


class rule_015(indent_rule):
    '''
    Port rule 015 checks the indentation of closing parenthesis for port maps.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'port', '015', 'isEndPortMap', 'isPortDeclaration')
        self.solution = 'Ensure proper indentation.'
