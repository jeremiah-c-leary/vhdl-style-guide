
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_block_label)


class rule_506(token_case_with_prefix_suffix):
    '''
    This rule checks the label has proper case on the end block declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end block BLOCK_LABEL;

    **Fix**

    .. code-block:: vhdl

       end block block_label;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'block', '506', lTokens)
        self.groups.append('case::label')
