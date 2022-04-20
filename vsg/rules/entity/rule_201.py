
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token as Rule

from vsg.token import entity_declaration as token


class rule_201(Rule):
    '''
    This rule ensures no blank lines after the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       entity fifo is


         port (

    **Fix**

    .. code-block:: vhdl

       entity fifo is
         port (
    '''
    def __init__(self):
        Rule.__init__(self, 'entity', '201', [token.is_keyword], iAllow=0)
