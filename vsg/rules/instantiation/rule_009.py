
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.instantiated_unit.component_name)


class rule_009(token_case_with_prefix_suffix):
    '''
    This rule checks the component name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       u_fifo : FIFO


    **Fix**

    .. code-block:: vhdl

       u_fifo : fifo
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'instantiation', '009', lTokens)
        self.groups.append('case::name')
