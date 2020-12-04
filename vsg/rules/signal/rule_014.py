
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.signal_declaration.identifier)

lIgnore = []
lIgnore.append(token.interface_signal_declaration.identifier)
lIgnore.append(token.interface_unknown_declaration.identifier)
lIgnore.append(token.interface_constant_declaration.identifier)
lIgnore.append(token.interface_variable_declaration.identifier)
lIgnore.append(token.association_element.formal_part)
lIgnore.append(token.entity_declaration.identifier)
lIgnore.append(token.entity_declaration.entity_simple_name)
lIgnore.append(token.architecture_body.entity_name)
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_014(consistent_token_case):
    '''
    Constant rule 014 checks case consistency of signal names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'signal', '014', lTokens, lIgnore)
