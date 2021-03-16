
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.full_type_declaration.is_keyword, token.enumeration_type_definition.open_parenthesis])
lTokens.append([token.full_type_declaration.is_keyword, token.range_constraint.range_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.unbounded_array_definition.array_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.constrained_array_definition.array_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.record_type_definition.record_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.access_type_definition.access_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.file_type_definition.file_keyword])


class rule_007(single_space_between_token_pairs):
    '''
    Checks for a single space after the *is* keyword.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'type', '007', lTokens)
        self.solution = 'Ensure only a single space after the *is* keyword.'
