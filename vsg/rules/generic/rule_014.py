
from vsg.rules import single_space_before_character_rule


class rule_014(single_space_before_character_rule):
    '''
    Generic rule 014 checks for at least a single space before the :.
    '''

    def __init__(self):
        single_space_before_character_rule.__init__(self, 'generic', '014', 'isGenericDeclaration', ':')
        self.solution = 'Add a space before the :.'
