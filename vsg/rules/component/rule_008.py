
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.identifier)


class rule_008(token_case_with_prefix_suffix):
    '''
    This rule checks the component name has proper case in the component declaration.

    Refer to `Configuring Uppercase and Lowercase Rules <configuring_uppercase_and_lowercase_rules.html>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       component FIFO is

    **Fix**

    .. code-block:: vhdl

       component fifo is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'component', '008', lTokens)
        self.groups.append('case::name')
