
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.use_clause.package_name)


class rule_501(Rule):
    '''
    This rule checks the package name called out in the selected name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       use ieee.STD_LOGIC_1164.all;

    **Fix**

    .. code-block:: vhdl

       use ieee.std_logic_1164.all;
    '''

    def __init__(self):
        Rule.__init__(self, 'use_clause', '501', lTokens)
        self.groups.append('case::name')
        self.configuration.append('case_exceptions')
