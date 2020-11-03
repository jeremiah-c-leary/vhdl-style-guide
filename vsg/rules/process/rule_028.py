
from vsg.rules import align_left_token_with_right_token_if_right_token_starts_a_line

from vsg import token

oLeftToken = token.process_statement.open_parenthesis
oRightToken = token.process_statement.close_parenthesis


class rule_028(align_left_token_with_right_token_if_right_token_starts_a_line):
    '''
    Checks for the proper indentation at the beginning of the process specification.
    '''

    def __init__(self):
        align_left_token_with_right_token_if_right_token_starts_a_line.__init__(self, 'process', '028', oLeftToken, oRightToken)
