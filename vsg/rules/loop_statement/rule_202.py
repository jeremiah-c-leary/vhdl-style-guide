
from vsg.rules import previous_line

from vsg.token import loop_statement as token

lTokens = []
lTokens.append(token.end_keyword)


class rule_202(previous_line):
    '''
    This rule checks for blank lines or comments above the **end** keyword.

    Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

    **Violation**

    .. code-block:: vhdl

       loop
         a <= b;
       end loop;

    **Fix**

    .. code-block:: vhdl

       loop
         a <= b;

       end loop;
    '''
    def __init__(self):
        previous_line.__init__(self, 'loop_statement', '202', lTokens)
