# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_after_tokens_in_between_tokens import Rule

lTokens = []
lTokens.append(token.association_element.assignment)

oStart = token.procedure_call.open_parenthesis
oEnd = token.procedure_call.close_parenthesis


class rule_101(Rule):
    """
    This rule checks for a single space after the **=>** operator in procedure calls.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       connect_ports(
         port_1 =>    data,
         port_2 =>enable,
         port_3 =>  overflow,
         port_4 => underflow
       );

    **Fix**

    .. code-block:: vhdl

       connect_ports(
         port_1 => data,
         port_2 => enable,
         port_3 => overflow,
         port_4 => underflow
       );
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
