
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.logical_operator.and_operator)
lTokens.append(token.logical_operator.or_operator)
lTokens.append(token.logical_operator.nand_operator)
lTokens.append(token.logical_operator.nor_operator)
lTokens.append(token.logical_operator.xor_operator)
lTokens.append(token.logical_operator.xnor_operator)


class rule_500(token_case):
    '''
    This rule checks logical operators have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       a <= b AND c;

    **Fix**

    .. code-block:: vhdl

       a <= b and c;
    '''

    def __init__(self):
        token_case.__init__(self, 'logical_operator', '500', lTokens)
        self.groups.append('case::keyword')
