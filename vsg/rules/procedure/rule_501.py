
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.designator)


class rule_501(token_case_with_prefix_suffix):
    '''
    This rule checks the procedure designator has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       procedure AVERAGE_SAMPLES is

    **Fix**

    .. code-block:: vhdl

       procedure average_samples is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'procedure', '501', lTokens)
        self.groups.append('case::name')
