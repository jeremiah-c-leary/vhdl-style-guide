
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import architecture_body as token


class rule_022(Rule):
    '''
    This rule checks for a single space before the entity name in the end architecture declaration.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end architecture    fifo;

    **Fix**

    .. code-block:: vhdl

       end architecture fifo;
    '''
    def __init__(self):
        Rule.__init__(self, 'architecture', '022')
        self.left_token = token.end_architecture_keyword
        self.right_token = token.architecture_simple_name
