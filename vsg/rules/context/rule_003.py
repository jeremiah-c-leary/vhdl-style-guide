
from vsg.rules import previous_line

from vsg.token import context_declaration as token


class rule_003(previous_line):
    '''
    This rule checks for blank lines or comments above the **context** keyword.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       library ieee;
       context c1 is

       --Some Comment
       context c1 is

    **Fix**

    .. code-block:: vhdl

       library ieee;

       context c1 is

       --Some Comment
       context c1 is
    '''

    def __init__(self):
        previous_line.__init__(self, 'context', '003', [token.context_keyword])
        self.style = 'no_code'
