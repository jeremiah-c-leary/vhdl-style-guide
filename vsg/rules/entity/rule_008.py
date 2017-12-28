
from vsg.rules import uppercase_word_rule


class rule_008(uppercase_word_rule):
    '''
    Entity rule 008 checks the entity name is uppercase in the entity declaration line.
    '''

    def __init__(self):
        uppercase_word_rule.__init__(self, 'entity', '008', 'isEntityDeclaration', 1)
        self.solution = 'Change entity name to all uppercase.'
