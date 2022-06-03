
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import loop_statement as token


class rule_101(Rule):
    '''
    This rule checks for a single space before the ending loop label if it exists.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end loop           END_LOOP_LABEL;

    **Fix**

    .. code-block:: vhdl

       end loop END_LOOP_LABEL;
    '''
    def __init__(self):
        Rule.__init__(self, 'loop_statement', '101')
        self.left_token = token.end_loop_keyword
        self.right_token = token.end_loop_label
