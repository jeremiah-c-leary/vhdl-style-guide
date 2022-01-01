
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_009(token_case):
    '''
    This rule checks the **end** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       END architecture;

       End architecture;

    **Fix**

    .. code-block:: vhdl

       end architecture;

       end architecture;
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '009', [token.end_keyword])
        self.groups.append('case::keyword')
