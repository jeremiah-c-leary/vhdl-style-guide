
from vsg.rules import single_space_after_character_rule


class rule_005(single_space_after_character_rule):
    '''Generic rule 005 checks for a single space after the colon in a generic declaration.'''

    def __init__(self):
        single_space_after_character_rule.__init__(self, 'generic', '005', 'isGenericDeclaration', ':')
        self.solution = 'Reduce number of spaces after the colon to 1.'
