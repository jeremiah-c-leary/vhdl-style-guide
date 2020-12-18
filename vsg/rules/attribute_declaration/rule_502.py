
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.type_mark.name)

oStartToken = token.attribute_declaration.colon

oEndToken = token.attribute_declaration.semicolon


class rule_502(token_case_in_range_bounded_by_tokens):
    '''
    Checks the identifier has proper case.
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'attribute_declaration', '502', lTokens, oStartToken, oEndToken)
