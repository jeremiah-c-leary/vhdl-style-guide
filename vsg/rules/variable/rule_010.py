
from vsg.rules import token_case_n_token_after_tokens

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.colon)


class rule_010(token_case_n_token_after_tokens):
    '''
    This rule checks the variable type has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable count : INTEGER;

    **Fix**

    .. code-block:: vhdl

       variable count : integer;
    '''

    def __init__(self):
        token_case_n_token_after_tokens.__init__(self, 'variable', '010', 1, lTokens)
        self.disabled = True
        self.configuration.append('prefix_exceptions')
        self.configuration.append('suffix_exceptions')
        self.groups.append('case::name')
