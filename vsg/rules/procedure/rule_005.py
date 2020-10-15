
from vsg.rules import token_indent_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.use_clause.keyword)
lTokens.append(token.variable_declaration.variable_keyword)
lTokens.append(token.constant_declaration.constant_keyword)

oStart = token.subprogram_body.is_keyword
oEnd = token.subprogram_body.begin_keyword


class rule_005(token_indent_between_tokens):
    '''
    Checks the indent of procedure parameters when they are on multiple lines.
    '''

    def __init__(self):
        token_indent_between_tokens.__init__(self, 'procedure', '005', lTokens, oStart, oEnd)
