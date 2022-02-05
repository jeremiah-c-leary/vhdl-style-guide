
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_004(previous_line):
    '''
    This rule checks for blank lines or comments above the instantiation.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       WR_EN <= '1';
       U_FIFO : FIFO

       -- Instantiate another FIFO
       U_FIFO2 : FIFO

    **Fix**

    .. code-block:: vhdl

       WR_EN <= '1';

       U_FIFO : FIFO

       -- Instantiate another FIFO
       U_FIFO2 : FIFO
    '''

    def __init__(self):
        previous_line.__init__(self, 'instantiation', '004', lTokens)
        self.style = 'no_code'
