
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token as Rule

from vsg.token import case_statement as token


class rule_202(Rule):
    '''
    This rule ensures a single blank line after the **context** keword.

    **Violation**

    .. code-block:: vhdl

       case state is



         when state1 =>

    **Fix**

    .. code-block:: vhdl

       case state is

         when state1 =>
    '''
    def __init__(self):
        Rule.__init__(self, 'case', '202', [token.is_keyword])
