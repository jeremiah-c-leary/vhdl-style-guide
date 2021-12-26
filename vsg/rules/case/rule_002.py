
from vsg import parser

from vsg.rules import single_space_between_tokens

from vsg.token import case_statement as token


class rule_002(single_space_between_tokens):
    '''
    This rule checks for a single space after the **case** keyword.

    **Violation**

    .. code-block:: vhdl

       case    data is


    **Fix**

    .. code-block:: vhdl

       case data is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'case', '002', token.case_keyword, parser.todo)
        self.solution = 'Reduce spaces between *case* keyword and expression.'
