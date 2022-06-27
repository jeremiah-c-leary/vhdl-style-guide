
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import loop_statement as token


class rule_100(Rule):
    '''
    This rule checks that a single space exists between the **end** and **loop** keywords

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

         end loop;
         end    loop;

    **Fix**

    .. code-block:: vhdl

         end loop;
         end loop;
    '''
    def __init__(self):
        Rule.__init__(self, 'loop_statement', '100')
        self.left_token = token.end_keyword
        self.right_token = token.end_loop_keyword
