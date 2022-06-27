
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import architecture_body as token


class rule_033(Rule):
    '''
    This rule checks for a single space between the entity_name and the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo    is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''
    def __init__(self):
        Rule.__init__(self, 'architecture', '033')
        self.left_token = token.entity_name
        self.right_token = token.is_keyword
