
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.end_keyword)


class rule_008(token_case):
    '''
    This rule checks the **end** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       END;

       End procedure proc;

    **Fix**

    .. code-block:: vhdl

       end;

       end procedure proc;
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '008', lTokens)
        self.groups.append('case::keyword')
