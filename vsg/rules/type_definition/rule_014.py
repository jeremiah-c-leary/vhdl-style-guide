
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.incomplete_type_declaration.identifier)
lTokens.append(token.full_type_declaration.identifier)

lIgnore = []
lIgnore.append(token.interface_signal_declaration.identifier)
lIgnore.append(token.interface_unknown_declaration.identifier)
lIgnore.append(token.interface_constant_declaration.identifier)
lIgnore.append(token.interface_variable_declaration.identifier)
lIgnore.append(token.association_element.formal_part)
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_014(consistent_token_case):
    '''
    Constant rule 014 checks case consistency of type names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'type', '014', lTokens, lIgnore)
