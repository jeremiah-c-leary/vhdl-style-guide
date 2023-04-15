

from vsg.rules import move_token_right_to_next_non_whitespace_token as Rule

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)


class rule_037(Rule):
    '''
    This rule checks a label and the colon are on the same line.

    **Violation**

    .. code-block:: vhdl

       label
       :

    **Fix**

    .. code-block:: vhdl

       label :
    '''

    def __init__(self):
        Rule.__init__(self, 'process', '037', lTokens)
        self.subphase = 3
