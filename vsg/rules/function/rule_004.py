
from vsg.rules import token_case_in_range_bounded_by_tokens

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.begin_keyword)

oStartToken = token.function_specification.function_keyword
oEndToken = token.subprogram_body.semicolon


class rule_004(token_case_in_range_bounded_by_tokens):
    '''
    This rule checks the **begin** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
       BEGIN

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
       begin
    '''

    def __init__(self):
        token_case_in_range_bounded_by_tokens.__init__(self, 'function', '004', lTokens, oStartToken, oEndToken)
        self.groups.append('case::keyword')
