
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import context_declaration as token


class rule_019(Rule):
    '''
    This rule checks for a single space between the **context** keyword and the context identifier.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end context;

       end context    c1;

    **Fix**

    .. code-block:: vhdl

       end context;

       end context c1;
    '''
    def __init__(self):
        Rule.__init__(self, 'context', '019')
        self.left_token = token.end_context_keyword
        self.right_token = token.context_simple_name
