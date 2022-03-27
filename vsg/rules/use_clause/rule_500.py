
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.use_clause.library_name)


class rule_500(Rule):
    '''
    This rule checks the library name called out in the selected name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       use IEEE.std_logic_1164.all;

       use my_LIB.all;

    **Fix**

    .. code-block:: vhdl

       use ieee.std_logic_1164.all;

       use my_lib.all;
    '''

    def __init__(self):
        Rule.__init__(self, 'use_clause', '500', lTokens)
        self.groups.append('case::name')
        self.configuration.append('case_exceptions')
