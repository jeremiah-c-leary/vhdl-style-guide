
from vsg.rules import consistent_token_case

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.identifier)

lIgnore = []
lIgnore.append(token.interface_signal_declaration.identifier)
lIgnore.append(token.interface_unknown_declaration.identifier)
lIgnore.append(token.interface_constant_declaration.identifier)
lIgnore.append(token.interface_variable_declaration.identifier)
lIgnore.append(token.association_element.formal_part)
lIgnore.append(token.entity_declaration.identifier)
lIgnore.append(token.entity_declaration.entity_simple_name)
lIgnore.append(token.architecture_body.entity_name)


class rule_013(consistent_token_case):
    '''
    Constant rule 013 checks case consistency of constant names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'constant', '013', lTokens, lIgnore)
