
from vsg.rules import indent_rule


class rule_004(indent_rule):
    '''
    Port rule 004 checks indentation of ports.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'port', '004', 'isPortDeclaration', 'isEndPortMap')
        self.solution = 'Ensure proper indentation.'
