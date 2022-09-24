
from vsg.rules import multiline_alignment_between_tokens as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.procedure_call.procedure_name, token.procedure_call.close_parenthesis])


class rule_400(Rule):
    '''
    This rule checks the alignment of multiline procedure calls.

    **Violation**

    .. code-block:: vhdl

       connect_ports(port_1, port_2, port_3,
             port_4, port_5,
                          port_6, port_7);

    **Fix**

    .. code-block:: vhdl

       connect_ports(port_1, port_2, port_3,
                     port_4, port_5,
                     port_6, port_7);
    '''

    def __init__(self):
        Rule.__init__(self, 'procedure_call', '400', lTokenPairs)
        self.phase = 5
