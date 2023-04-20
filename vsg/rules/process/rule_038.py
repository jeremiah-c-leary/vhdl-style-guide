

from vsg.rules import move_token_right_to_next_non_whitespace_token as Rule

from vsg import token

lTokens = []
lTokens.append(token.process_statement.label_colon)


class rule_038(Rule):
    '''
    This rule checks a label colon is on the same line as the **process** or **postponed** keyword.

    **Violation**

    .. code-block:: vhdl

       label :
       process

    **Fix**

    .. code-block:: vhdl

       label
       : process
    '''

    def __init__(self):
        Rule.__init__(self, 'process', '038', lTokens)
        self.subphase = 2
