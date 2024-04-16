# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens as Rule

lAlign = []
lAlign.append(token.association_element.assignment)

oBegin = token.procedure_call.open_parenthesis
oEnd = token.procedure_call.close_parenthesis


class rule_401(Rule):
    """
    This rule checks the alignment of :code:`=>` keywords in procedure calls.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       connect_ports(
         port_1=> data,
         port_2 => enable,
         port_3    => overflow,
         port_4  => underflow
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
        super().__init__(lAlign, oBegin, oEnd)
        self.solution = "Align =>."
        self.subphase = 2
        self.bIncludeTillBeginningOfLine = True
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
