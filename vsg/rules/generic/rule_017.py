
from vsg.rules import token_case_n_token_after_tokens_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.colon)
lTokens.append(token.interface_variable_declaration.colon)
lTokens.append(token.interface_signal_declaration.colon)
lTokens.append(token.interface_unknown_declaration.colon)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis


class rule_017(token_case_n_token_after_tokens_between_tokens):
    '''
    This rule checks the generic type has proper case if it is a VHDL keyword.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

      generic (
        g_width : STD_LOGIC := '0';
        g_depth : Std_logic := '1'
      );

    **Fix**

    .. code-block:: vhdl

      generic (
        g_width : std_logic := '0';
        g_depth : std_logic := '1'
      );
    '''

    def __init__(self):
        token_case_n_token_after_tokens_between_tokens.__init__(self, 'generic', '017', 1, lTokens, oStart, oEnd, True)
        self.disabled = True
        self.groups.append('case::keyword')
