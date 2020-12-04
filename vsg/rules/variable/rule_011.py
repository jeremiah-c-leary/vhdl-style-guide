
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.variable_declaration.identifier)

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


class rule_011(consistent_token_case):
    '''
    Constant rule 011 checks case consistency of variable names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'variable', '011', lTokens, lIgnore)
