
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import architecture_body as token


class rule_031(Rule):
    '''
    This rule checks for a single space between the name and the **of** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl    of fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''
    def __init__(self):
        Rule.__init__(self, 'architecture', '031')
        self.left_token = token.identifier
        self.right_token = token.of_keyword
