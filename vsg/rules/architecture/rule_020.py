
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_020(token_case):
    '''
    This rule checks the proper case of the **is** keyword in the architecture declaration.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo IS

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '020', [token.is_keyword])
        self.groups.append('case::keyword')
