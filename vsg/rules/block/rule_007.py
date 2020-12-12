
from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token

from vsg.token import block_statement as token

oInsertToken = token.end_block_label

oAnchorToken = token.semicolon

oLeftToken = token.end_keyword
oRightToken = token.semicolon

oValueToken = token.block_label


class rule_007(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    '''
    Checks the process name exists on the same line as the "end" and "process" keywords.
    '''

    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token.__init__(self, 'block', '007', oInsertToken, oAnchorToken, oLeftToken, oRightToken, oValueToken)
        self.solution = 'label'
