
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.procedure_keyword)


class rule_200(previous_line):
    '''
    This rule checks for blank lines or comments above the **procedure** keyword.

    Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

    **Violation**

    .. code-block:: vhdl

       architecture RTL of FIFO is
         procedure proc1 is


    **Fix**

    .. code-block:: vhdl

       architecture RTL of FIFO is

         procedure proc1 is
    '''

    def __init__(self):
        previous_line.__init__(self, 'procedure', '200', lTokens)
