
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import case_statement as token


class rule_006(Rule):
    '''
    This rule checks for a single space between the **end** and **case** keywords.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      case data is

      end    case;

    **Fix**

    .. code-block:: vhdl

      case data is

      end case;
    '''
    def __init__(self):
        Rule.__init__(self, 'case', '006')
        self.left_token = token.end_keyword
        self.right_token = token.end_case_keyword
