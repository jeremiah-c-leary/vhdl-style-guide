
from vsg.rules import token_case_n_token_after_tokens

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.colon)


class rule_010(token_case_n_token_after_tokens):
    '''
    This rule checks the signal type has proper case if it is a VHDL keyword.

    .. NOTE:: This rule is disabled by default.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       signal wr_en   : STD_LOGIC;
       signal rd_en   : Std_logic;
       signal cs_f    : t_User_Defined_Type;

    **Fix**

    .. code-block:: vhdl

       signal wr_en   : std_logic;
       signal rd_en   : std_logic;
       signal cs_f    : t_User_Defined_Type;
    '''

    def __init__(self):
        token_case_n_token_after_tokens.__init__(self, 'signal', '010', 1, lTokens)
        self.disabled = True
        self.bLimitToVhdlKeywords = True
        self.groups.append('case::keyword')
