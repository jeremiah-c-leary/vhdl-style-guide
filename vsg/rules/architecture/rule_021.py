
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_021(token_case):
    '''
    This rule checks the proper case of the **begin** keyword.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is
       BEGIN

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '021', [token.begin_keyword])
        self.groups.append('case::keyword')
