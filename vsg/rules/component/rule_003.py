
from vsg.rules import previous_line

from vsg.token import component_declaration as token


class rule_003(previous_line):
    '''
    This rule checks for blank lines or comments above the **component** declaration.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       end component fifo;
       component ram is

    **Fix**

    .. code-block:: vhdl

       end component fifo;

       component ram is
    '''

    def __init__(self):
        previous_line.__init__(self, 'component', '003', [token.component_keyword])
        self.style = 'no_code'
