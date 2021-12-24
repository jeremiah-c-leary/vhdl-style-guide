
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.variable_declaration.colon)
lAlign.append(token.constant_declaration.colon)


class rule_401(align_tokens_in_region_between_tokens):
    '''
    This rule checks the colons are in the same column for all declarations in the procedure declarative part.
    Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.
    
    **Violation**
    
    .. code-block:: vhdl
    
       signal sig1: natural;
       variable var2  : natural;
       constant c_period : time;
       file my_test_input : my_file_type;
    
    **Fix**
    
    .. code-block:: vhdl
    
       signal sig1        : natural;
       variable var2      : natural;
       constant c_period  : time;
       file my_test_input : my_file_type;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'procedure', '401', lAlign, token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword)
        self.solution = 'Align :.'
        self.subphase = 2
