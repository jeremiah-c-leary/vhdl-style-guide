
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_008(token_case_with_prefix_suffix):
    '''
    This rule checks the instance label has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       U_FIFO : fifo

    **Fix**

    .. code-block:: vhdl

       u_fifo : fifo
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'instantiation', '008', lTokens)
        self.groups.append('case::label')
