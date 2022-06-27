
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import architecture_body as token


class rule_032(Rule):
    '''
    This rule checks for a single space between the **of** keyword and the entity_name.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of    fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''
    def __init__(self):
        Rule.__init__(self, 'architecture', '032')
        self.left_token = token.of_keyword
        self.right_token = token.entity_name
