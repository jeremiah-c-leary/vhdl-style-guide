
from vsg.rules import single_space_after_character_rule


class rule_002(single_space_after_character_rule):
    '''
    Instantiation rule 002 checks for a single space after the :
    '''

    def __init__(self):
        single_space_after_character_rule.__init__(self, 'instantiation', '002', 'isInstantiationDeclaration', ':')
        self.solution = 'Ensure only one space after the :.'
