
from vsg.rules import token_indent_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)
lTokens.append(token.component_instantiation_statement.semicolon)

lTokens.append(token.generic_map_aspect.generic_keyword)
lTokens.append(token.generic_map_aspect.close_parenthesis)

lTokens.append(token.port_map_aspect.port_keyword)
lTokens.append(token.port_map_aspect.close_parenthesis)

lTokens.append(token.association_element.formal_part)

oStart = token.component_instantiation_statement.instantiation_label
oEnd = token.component_instantiation_statement.semicolon


class rule_001(token_indent_between_tokens):
    '''
    Checks the indent of instantiation elements.
    '''

    def __init__(self):
        token_indent_between_tokens.__init__(self, 'instantiation', '001', lTokens, oStart, oEnd, bInclusive=True)
