
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import component_declaration as token


class rule_011(Rule):
    '''
    This rule checks for single space after the **end** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end   component fifo;

    **Fix**

    .. code-block:: vhdl

       end component fifo;
    '''
    def __init__(self):
        Rule.__init__(self, 'component', '011')
        self.left_token = token.end_keyword
        self.right_token = token.end_component_keyword
