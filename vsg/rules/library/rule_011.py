
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.use_clause.keyword)


class rule_011(split_line_at_token):
    '''
    This rule checks the **use** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       context c1 is library ieee; use ieee.std_logic_1164.all; end context c1;

    **Fix**

    .. code-block:: vhdl

       context c1 is library ieee;
           use ieee.std_logic_1164.all; end context c1;
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'library', '011', lTokens)
        self.solution = 'Move *use* to it\'s own line.'
