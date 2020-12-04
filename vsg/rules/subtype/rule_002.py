
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.subtype_declaration.identifier)

lIgnore = []
lIgnore.append(token.interface_signal_declaration.identifier)
lIgnore.append(token.interface_unknown_declaration.identifier)
lIgnore.append(token.interface_constant_declaration.identifier)
lIgnore.append(token.interface_variable_declaration.identifier)
lIgnore.append(token.association_element.formal_part)
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_002(consistent_token_case):
    '''
    Constant rule 002 checks case consistency of subtype names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'subtype', '002', lTokens, lIgnore)
