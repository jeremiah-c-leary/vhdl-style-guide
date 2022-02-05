
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist_before_token

from vsg.token import package_declaration as token


class rule_007(insert_token_right_of_token_if_it_does_not_exist_before_token):
    '''
    This rule checks for the **package** keyword on the end package declaration.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

       end package FIFO_PKG;
    '''

    def __init__(self):
        insert_token_right_of_token_if_it_does_not_exist_before_token.__init__(self, 'package', '007', token.end_package_keyword('package'), token.end_keyword, token.semicolon)
        self.solution = '*package* keyword'
