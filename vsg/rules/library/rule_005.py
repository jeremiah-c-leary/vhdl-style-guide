
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.use_clause.keyword)


class rule_005(token_case):
    '''
    This rule checks the **use** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       library ieee;
         USE ieee.std_logic_1164.all;
         Use ieee.std_logic_unsigned.all;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         use ieee.std_logic_1164.all;
         use ieee.std_logic_unsigned.all;
    '''

    def __init__(self):
        token_case.__init__(self, 'library', '005', lTokens)
        self.groups.append('case::keyword')
