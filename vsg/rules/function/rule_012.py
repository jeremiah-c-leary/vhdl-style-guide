
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.variable_declaration.colon)
lAlign.append(token.constant_declaration.colon)

oStartToken = token.subprogram_body.is_keyword
oEndToken = token.subprogram_body.begin_keyword

lUnless = []
lUnless.append([token.procedure_specification.procedure_keyword, token.subprogram_body.semicolon])


class rule_012(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    This rule checks the colons are in the same column for all declarations in the function declarative part.

    Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

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
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'function', '012', lAlign, oStartToken, oEndToken, lUnless)
        self.solution = 'Align :.'
        self.subphase = 2
