
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_kind.procedure_keyword])
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_body.designator])
lTokens.append([token.subprogram_kind.procedure_keyword, token.subprogram_body.designator])


class rule_101(Rule):
    '''
    This rule checks for a single space between the **end** and **procedure** keywords and procedure designator.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end   procedure   average_samples;
       end   procedure;
       end   average_samples;

    **Fix**

    .. code-block:: vhdl

       end procedure average_samples;
       end procedure;
       end average_samples;
    '''
    def __init__(self):
        Rule.__init__(self, 'procedure', '101', lTokens)
