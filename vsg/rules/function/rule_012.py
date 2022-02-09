
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens as Rule

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.variable_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.alias_declaration.colon)
lAlign.append(token.alias_declaration.is_keyword)

oStartToken = token.subprogram_body.is_keyword
oEndToken = token.subprogram_body.begin_keyword

lUnless = []
lUnless.append([token.procedure_specification.procedure_keyword, token.subprogram_body.semicolon])


class rule_012(Rule):
    '''
    This rule checks the colons are in the same column for all declarations in the function declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable var1 : natural;
       variable var2  : natural;
       constant c_period : time;

    **Fix**

    .. code-block:: vhdl

       variable var1     : natural;
       variable var2     : natural;
       constant c_period : time;
    '''

    def __init__(self):
        Rule.__init__(self, 'function', '012', lAlign, oStartToken, oEndToken, lUnless)
        self.solution = 'Align :.'
        self.subphase = 2
