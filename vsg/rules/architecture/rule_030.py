
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import architecture_body as token


class rule_030(Rule):
    '''
    This rule checks for a single space between **architecture** and the name.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture    rtl of fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''
    def __init__(self):
        Rule.__init__(self, 'architecture', '030')
        self.left_token = token.architecture_keyword
        self.right_token = token.identifier
