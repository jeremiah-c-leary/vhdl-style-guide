
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import process_statement as token

oInsertToken = token.end_process_label

oAnchorToken = token.semicolon

oLeftToken = token.end_keyword
oRightToken = token.semicolon

oValueToken = token.process_label


class rule_018(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    This rule checks the **end process** line has a label.
    The closing label will be added if the opening process label exists.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end process;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'process', '018', oInsertToken, oAnchorToken, oLeftToken, oRightToken, oValueToken)
        self.solution = 'a label for the "end process".'
        self.subphase = 2
