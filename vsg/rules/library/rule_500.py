
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.logical_name_list.logical_name)


class rule_500(token_case):
    '''
    This rule checks the logical_name in a library_clause has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       library IEEE;

       library FIFO_dsn;

    **Fix**

    .. code-block:: vhdl

       library ieee;

       library fifo_dsn;
    '''

    def __init__(self):
        token_case.__init__(self, 'library', '500', lTokens)
        self.groups.append('case::name')
        self.configuration.append('case_exceptions')
