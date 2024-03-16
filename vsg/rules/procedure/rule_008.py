# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.subprogram_body.end_keyword)

oStartToken = token.procedure_specification.procedure_keyword
oEndToken = token.subprogram_body.semicolon


class rule_008(token_case_in_range_bounded_by_tokens):
    '''
    This rule checks the **end** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       END;

       End procedure proc;

    **Fix**

    .. code-block:: vhdl

       end;

       end procedure proc;
    '''

    def __init__(self):
        super().__init__(lTokens, oStartToken, oEndToken)
        self.groups.append('case::keyword')
