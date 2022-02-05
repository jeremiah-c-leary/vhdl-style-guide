
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_200(previous_line):
    '''
    This rule checks for blank lines or comments above the block label.

    |configuring_previous_line_rules_link|

    **Violation**

    .. code-block:: vhdl

       a <= b;
       block_label : block is

    **Fix**

    .. code-block:: vhdl

       a <= b;

       block_label : block is
    '''

    def __init__(self):
        previous_line.__init__(self, 'block', '200', lTokens)
