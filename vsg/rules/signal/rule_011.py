
from vsg import token

from vsg.rules import token_case_subtype_indication

lStartTokens = []
lStartTokens.append(token.signal_declaration.colon)

lEndTokens = []
lEndTokens.append(token.signal_declaration.assignment_operator)
lEndTokens.append(token.signal_declaration.semicolon)
lEndTokens.append(token.signal_kind.register_keyword)
lEndTokens.append(token.signal_kind.bus_keyword)


class rule_011(token_case_subtype_indication):
    '''
    This rule checks the signal type has proper case.

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
       signal cs_f    : t_user_defined_type;
    '''

    def __init__(self):
        token_case_subtype_indication.__init__(self, 'signal', '011', lStartTokens, lEndTokens)
        self.groups.append('case::name')
