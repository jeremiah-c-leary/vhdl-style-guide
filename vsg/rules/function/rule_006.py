
from vsg.rules import previous_line

from vsg.token import function_specification as token

lTokens = []
lTokens.append(token.function_keyword)
lTokens.append(token.pure_keyword)
lTokens.append(token.impure_keyword)


class rule_006(previous_line):
    '''
    This rule checks for blank lines or comments above the **function** keyword.

    |configuring_previous_line_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture RTL of FIFO is
         function overflow (a: integer) return integer is


    **Fix**

    .. code-block:: vhdl

       architecture RTL of FIFO is

         function overflow (a: integer) return integer is
    '''

    def __init__(self):
        previous_line.__init__(self, 'function', '006', lTokens)
