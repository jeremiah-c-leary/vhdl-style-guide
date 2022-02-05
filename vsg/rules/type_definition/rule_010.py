
from vsg import token

from vsg.rules import previous_line

lTokens = []
lTokens.append(token.incomplete_type_declaration.type_keyword)
lTokens.append(token.full_type_declaration.type_keyword)


class rule_010(previous_line):
    '''
    This rule checks for blank lines or comments above the **type** declaration.

    |configuring_previous_line_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal wr_en : std_logic;
       type state_machine is (idle, write, read, done);

    **Fix**

    .. code-block:: vhdl

       signal wr_en : std_logic;

       type state_machine is (idle, write, read, done);
    '''

    def __init__(self):
        previous_line.__init__(self, 'type', '010', lTokens)
