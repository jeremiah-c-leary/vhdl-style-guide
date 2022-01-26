
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_004(token_case):
    '''
    This rule checks the **library** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       Library ieee;

       LIBRARY fifo_dsn;

    **Fix**

    .. code-block:: vhdl

       library ieee;

       library fifo_dsn;
    '''

    def __init__(self):
        token_case.__init__(self, 'library', '004', lTokens)
        self.groups.append('case::keyword')
