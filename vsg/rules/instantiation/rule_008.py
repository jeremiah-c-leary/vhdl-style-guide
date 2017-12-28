
from vsg.rules import uppercase_word_rule


class rule_008(uppercase_word_rule):
    '''
    Instantiation rule 008 checks the instance name is uppercase in the instantiation declaration line.
    '''

    def __init__(self):
        uppercase_word_rule.__init__(self, 'instantiation', '008', 'isInstantiationDeclaration', 0)
        self.solution = 'Change instance name to all uppercase.'
