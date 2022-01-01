
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_003(token_case_with_prefix_suffix):
    '''
    This rule checks the proper case of the label on a foor loop.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

         LABEL : for index in 4 to 23 loop
         Label : for index in 0 to 100 loop

    **Fix**

    .. code-block:: vhdl

         label : for index in 4 to 23 loop
         label : for index in 0 to 100 loop
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'for_loop', '003', lTokens)
        self.groups.append('case::label')
