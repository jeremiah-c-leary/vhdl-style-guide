
from vsg.rules import single_space_after_character_rule


class rule_006(single_space_after_character_rule):
    '''
    Generic rule 006 checks for a single space after the default assignment in a generic declaration.
    '''

    def __init__(self):
        single_space_after_character_rule.__init__(self, 'generic', '006', 'isGenericDeclaration', ':=')
        self.solution = 'Reduce number of spaces after the default assignment to 1.'
