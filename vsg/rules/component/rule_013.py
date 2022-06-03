
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import component_declaration as token


class rule_013(Rule):
    '''
    This rule checks for a single space after the **component** keyword in the **end component** line.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end component    fifo;

    **Fix**

    .. code-block:: vhdl

       end component fifo;
    '''
    def __init__(self):
        Rule.__init__(self, 'component', '013')
        self.left_token = token.end_component_keyword
        self.right_token = token.component_simple_name
