
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.context_reference.library_name)


class rule_500(Rule):
    '''
    This rule checks the library name called out in the selected name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       context my_LIB.all;

    **Fix**

    .. code-block:: vhdl

       context my_lib.all;
    '''

    def __init__(self):
        Rule.__init__(self, 'context_ref', '500', lTokens)
        self.groups.append('case::name')
        self.configuration.append('case_exceptions')
