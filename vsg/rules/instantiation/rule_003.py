
from vsg.rules import single_space_before_character_rule


class rule_003(single_space_before_character_rule):
    '''
    Instantiation rule 003 checks for a single space before the :
    '''

    def __init__(self):
        single_space_before_character_rule.__init__(self, 'instantiation', '003', 'isInstantiationDeclaration', ':')
        self.solution = 'Ensure only one space before the :.'
