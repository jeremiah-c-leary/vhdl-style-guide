
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token as Rule

from vsg.token import loop_statement as token

oInsertToken = token.end_loop_label

oAnchorToken = token.semicolon

oLeftToken = token.end_loop_keyword
oRightToken = token.semicolon

oValueToken = token.loop_label


class rule_007(Rule):
    '''
    This rule checks the **end loop_statement** line has a label.
    The closing label will be added if the opening loop_statement label exists.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end loop;

    **Fix**

    .. code-block:: vhdl

       end loop LOOP_LABEL;
    '''

    def __init__(self):
        Rule.__init__(self, 'loop_statement', '007', oInsertToken, oAnchorToken, oLeftToken, oRightToken, oValueToken)
        self.solution = 'a label for the "end loop".'
        self.subphase = 2
        self.disable = True
