
from vsg import parser
from vsg import token

from vsg.rules import consistent_case_of_tokens_from_between_tokens_applied_to_region

lTokens = []
lTokens.append(token.interface_unknown_declaration.identifier)
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)

lIgnore = []
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)
lIgnore.append(token.identifier.identifier)

oStartToken = token.generic_clause.open_parenthesis
oEndToken = token.generic_clause.close_parenthesis

oRegionStart = token.port_clause.open_parenthesis
oRegionEnd = token.port_clause.close_parenthesis


class rule_600(consistent_case_of_tokens_from_between_tokens_applied_to_region):
    '''
    Checks capitalization consistency of function names.
    '''

    def __init__(self):
        consistent_case_of_tokens_from_between_tokens_applied_to_region.__init__(self, 'entity', '600', lTokens, oStartToken, oEndToken, oRegionStart, oRegionEnd, lIgnore)
