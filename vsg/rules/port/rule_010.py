
from vsg.rules import uppercase_word_rule


class rule_010(uppercase_word_rule):
    '''
    Port rule 010 checks port names are uppercase.
    '''

    def __init__(self):
        uppercase_word_rule.__init__(self, 'port', '010', 'isPortDeclaration', 0)
        self.solution = 'Uppercase port name.'
