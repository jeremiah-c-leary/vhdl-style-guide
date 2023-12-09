
from vsg.rules import blank_line_below_line_ending_with_token as Rule

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.semicolon)

lAllowTokens = []
lAllowTokens.append(token.signal_declaration.signal_keyword)


class rule_200(Rule):
    '''
    This rule checks for a blank line below a signal declaration unless there is another signal definition.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       signal   width  : integer := 32;
       signal   height : integer := 4;
       constant length : integer := 32;

    **Fix**

    .. code-block:: vhdl

       signal   width  : integer := 32;
       signal   height : integer := 4;

       constant length : integer := 32;
    '''

    def __init__(self):
        Rule.__init__(self, 'signal', '200', lTokens, lAllowTokens)
        self.disable = True
        self.configuration.remove('style')
