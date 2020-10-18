
from vsg.rules import token_indent_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.identifier_list.identifier)

oStart = token.record_type_definition.record_keyword
oEnd = token.record_type_definition.end_keyword

class rule_012(token_indent_between_tokens):
    '''
    Checks the indent of record elements.
    '''

    def __init__(self):
        token_indent_between_tokens.__init__(self, 'type', '012', lTokens, oStart, oEnd)
