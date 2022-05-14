
from vsg.rules import whitespace_before_token as Rule

from vsg.token import case_statement_alternative as token


class rule_005(Rule):
    '''
    This rule checks for a single space before the **=>** operator.

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
        self.solution = 'Reduce spaces before the assignment operator to a single space.'
