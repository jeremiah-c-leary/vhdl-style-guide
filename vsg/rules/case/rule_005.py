
from vsg.rules.whitespace_before_token import Rule

from vsg.token import case_statement_alternative as token


class rule_005(Rule):
    '''
    This rule checks for a single space before the **=>** operator.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      case data is

        when 3   =>

    **Fix**

    .. code-block:: vhdl

      case data is

        when 3 =>
    '''
    def __init__(self):
        Rule.__init__(self, 'case', '005', [token.assignment])
