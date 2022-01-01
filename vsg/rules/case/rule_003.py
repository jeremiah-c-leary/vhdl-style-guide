
from vsg import parser

from vsg.rules import single_space_between_tokens

from vsg.token import case_statement as token


class rule_003(single_space_between_tokens):
    '''
    This rule checks for a single space before the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       case data    is

    **Fix**

    .. code-block:: vhdl

       case data is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'case', '003', parser.todo, token.is_keyword)
        self.solution = 'Reduce spaces between the expression and the *is* keyword.'
