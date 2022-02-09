
from vsg.rules import previous_line

from vsg.token import case_statement as token


class rule_007(previous_line):
    '''
    This rule checks for blank lines or comments above the **case** keyword.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       a <= '1';
       case data is


       -- This is a comment
       case data is

    **Fix**

    .. code-block:: vhdl

       a <= '1';

       case data is


       -- This is a comment
       case data is
    '''

    def __init__(self):
        previous_line.__init__(self, 'case', '007', [token.case_keyword])
        self.style = 'no_code'
