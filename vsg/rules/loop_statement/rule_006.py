
from vsg.rules import token_does_not_exist_before_token as Rule
from vsg.token import loop_statement as token

oFirstToken = token.loop_label

oSecondToken = token.loop_keyword


class rule_006(Rule):
    '''
    This rule checks that loop statements have a label.

    **Violation**

    .. code-block:: vhdl

       loop

       while (condition) loop

       for x in range (31 downto 0) loop

    **Fix**

    .. code-block:: vhdl

       LOOP_LABEL : loop

       LOOP_LABEL : while (condition) loop

       LOOP_LABEL : for x in range (31 downto 0) loop
    '''

    def __init__(self):
        Rule.__init__(self, 'loop_statement', '006', oFirstToken, oSecondToken)
        self.solution = 'Add label for loop statement'
        self.fixable = False
        self.disable = True
