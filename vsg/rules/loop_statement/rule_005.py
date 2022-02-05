
from vsg import token

from vsg.rules import remove_carriage_return_after_token as Rule

lTokens = []
lTokens.append(token.loop_statement.label_colon)


class rule_005(Rule):
    '''
    This rule checks the loop label and the **while**, **for** or **loop** keywords are on the same line.

    **Violation**

    .. code-block:: vhdl

       LOOP_LABEL:
         loop

       LOOP_LABEL:
         while condition loop

       LOOP_LABEL:
         for x in range(15 downto 0) loop

    **Fix**

    .. code-block:: vhdl

       LOOP_LABEL: loop

       LOOP_LABEL: while condition loop

       LOOP_LABEL: for x in range(15 downto 0) loop
    '''

    def __init__(self):
        Rule.__init__(self, 'loop_statement', '005', lTokens, bInsertSpace=True)
        self.solution = 'Merge line below with label.'
