
from vsg.rules import move_token_next_to_another_token

from vsg.token import package_body as token


class rule_001(move_token_next_to_another_token):
    '''
    This rule checks the **is** keyword is on the same line as the **package** keyword.

    **Violation**

    .. code-block:: vhdl

       package body FIFO_PKG
       is

    **Fix**

    .. code-block:: vhdl

       package body FIFO_PKG is
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'package_body', '001', token.package_simple_name, token.is_keyword)
        self.solution = 'Ensure *is* keyword is on the same line as the "package" keyword.'
