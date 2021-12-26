
from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace

from vsg.token import case_statement as token


class rule_019(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    '''
    This rule checks for labels before the **case** keyword.
    The label should be removed.
    The preference is to have comments above the case statement.

    **Violation**

    .. code-block:: vhdl

          CASE_LABEL : case address is
          CASE_LABEL: case address is
          case address is

    **Fix**

    .. code-block:: vhdl

          case address is
          case address is
          case address is
    '''

    def __init__(self):
        remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace.__init__(self, 'case', '019', token.case_label, token.label_colon)
        self.solution = 'Remove Label'
