
from vsg.rules import single_space_before_token

from vsg.token import case_statement_alternative as token


class rule_005(single_space_before_token):
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
        single_space_before_token.__init__(self, 'case', '005', [token.assignment])
        self.solution = 'Reduce spaces before the assignment operator to a single space.'
