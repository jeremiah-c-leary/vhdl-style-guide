
from vsg import token

from vsg.rules import remove_carriage_return_after_token

lTokens = []
lTokens.append(token.if_statement.if_keyword)
lTokens.append(token.if_statement.elsif_keyword)


class rule_035(remove_carriage_return_after_token):
    '''
    This rule checks the expression after the **if** or **elsif** keyword starts on the same line.

    **Violation**

    .. code-block:: vhdl

       if
         a = '1' then

       elsif
         b = '1' then

    **Fix**

    .. code-block:: vhdl

       if a = '1' then

       elsif b = '1' then
    '''

    def __init__(self):
        remove_carriage_return_after_token.__init__(self, 'if', '035', lTokens, bInsertSpace=True)
        self.solution = 'Merge lines with **elsif** keyword and expression below.'
