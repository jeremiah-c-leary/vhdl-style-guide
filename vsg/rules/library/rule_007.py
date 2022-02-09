
from vsg.rules import previous_line

from vsg.token import use_clause as token

lTokens = []
lTokens.append(token.keyword)


class rule_007(previous_line):
    '''
    This rule checks for blank lines or comments above the **use** declaration.

    |configuring_blank_lines_link|

    The default style is :code:`no_blank_line`.

    **Violation**

    .. code-block:: vhdl

       library ieee;

         use ieee.std_logic_1164.all;

         use ieee.std_logic_unsigned.all;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         use ieee.std_logic_1164.all;
         use ieee.std_logic_unsigned.all;
    '''
    def __init__(self):
        previous_line.__init__(self, 'library', '007', lTokens)
        self.style = 'no_blank_line'
