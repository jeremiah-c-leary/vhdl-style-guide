
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.enumeration_type_definition.enumeration_literal)

lIgnore = []
lIgnore.append(token.interface_signal_declaration.identifier)
lIgnore.append(token.interface_unknown_declaration.identifier)
lIgnore.append(token.interface_constant_declaration.identifier)
lIgnore.append(token.interface_variable_declaration.identifier)
lIgnore.append(token.association_element.formal_part)
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_501(consistent_token_case):
    '''
    This rule checks for consistent capitalization of enumerated types.

    **Violation**

    .. code-block:: vhdl

       type state is (IDLE, WRITE, READ);

       state <= Idle;
       state <= write;
       state <= ReAd;

    **Fix**

    .. code-block:: vhdl

       type state is (IDLE, WRITE, READ);

       state <= IDLE;
       state <= WRITE;
       state <= READ;
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'type', '501', lTokens, lIgnore)
        self.subphase = 2
